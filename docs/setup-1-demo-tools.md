# Install the workshop tools
## Prerequisites
You'll need
- Helm, the Kubernetes package manager. It's available [here](https://helm.sh/docs/intro/install/)
- an OpenShift cluster - with admin rights. You can create one by following the instructions [here](http:/try.openshift.com)
- the OpenShift command line interface, _oc_ available [here](https://docs.openshift.com/container-platform/4.6/cli_reference/openshift_cli/getting-started-cli.html)

## Installation procedure
Do the following:
- Clone this repo and change directory into the root dir, _ml-workshop_ & create a variable for this directory
```
git clone https://github.com/masoodfaisal/ml-workshop
cd ml-workshop
export REPO_HOME=`pwd`
```
- On the OpenShift console, choose the _Copy Login Command_ as shown and paste the _oc login ..._ command it gives to a terminal.
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/29-copy-login-command.png)

- Create a new project on the terminal
```
oc new-project ml-workshop  
```

- On GUI, select click project ml-workshop to select it
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/30-select-ml-workshop-project.png)

- Before installation, you may need to get your OpenShift cluster administrator to adjust your limit ranges - or delete if this a test cluster without resource pressures. This is because, there are some moderate resource requirements associated with this workshop, e.g. Jenkins alone requires 4 vCPU and 4 Gi memory and there are other resource hungry elements as well. These are set here:
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/29-resource-limits.png)

- Install Jenkins Operator (this takes several minutes)
```
IGNORE - FOLLOW NEXT WORKAROUND cd $REPO_HOME/helm/jenkins-operator
IGNORE - FOLLOW NEXT WORKAROUND helm install ml-jenkins-operator .
```
WORKAROUND - INSTALL JENKINS OPERATOR ON GUI

- Install Open Data Hub Operator (this takes several minutes)
```
IGNORE - FOLLOW NEXT WORKAROUND cd $REPO_HOME/helm/odh-operator
IGNORE - FOLLOW NEXT WORKAROUND helm install ml-odh-operator .
```
WORKAROUND - INSTALL ODH OPERATOR ON GUI


At this point, on GUI go to Installed Operators and wait until both operators are installed

TODO - FIX REQUIREMENT TO DELETE AND MANUALLY INSTALL RADANALYTICS SPARK & SELDON - AS BY DEFAULT THEY STAY IN A PERPETUAL UPGRADE-PENDING STATE

Now install the tools themselves:
- Jenkins
```
cd $REPO_HOME/helm/jenkins
helm install ml-jenkins .
```

- Open Data Hub tools in cluding Jupyter, Spark
```
cd $REPO_HOME/helm/odh
helm install ml-odh .
```

- Minio - our object storage implemenation
```
cd $REPO_HOME/helm/minio
helm install ml-minio .
```

- Verta.ai - our model repository
```
cd $REPO_HOME/helm/modeldb
helm install ml-modeldb .
```

WHEN ALL COMPONENTS HAVE INSTALLED, TRY LOGGING INTO JUPYTER HUB UNDER THE ROUTES VIEW. IF YOU GET A '500 : Internal Server Error CERTIFICATE_VERIFY_FAILED' FOLLOW THE TEMPORARY WORKAROUND IN THE NEXT PARAGRAPH.

TEMPORARY WORKAROUND - Next we need a temporary workaround for the fact that Jupyter Hub in the Open Data has an invalid certificate. Go to Config Maps and click on _jupyterhub-cfg_ to open it

![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/31-workaround-jup-hub-cert-fail-1.png)


Select yaml view, scroll down to the section *jupyterhub_config.py* and paste this in as shown and save it.
```
c.OpenShiftOAuthenticator.validate_cert = False
```
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/31-workaround-jup-hub-cert-fail-2.png)

Go to the Pods view, filter on _Jupyter_, select the pod _jupyterhub-1-XXXXXX_ as shown
, choose _Delete Pod_ on the right. A similar named pod will recreate itself after a minute
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/31-workaround-jup-hub-cert-fail-3-delete-pod.png)


The next thing we need to do is install a custom Jupyter image that contains required libraries for the three data-science focused workshops. Run the following
```
cd $REPO_HOME/notebook-image
oc import-image ml-workshop-elyra --from='quay.io/ml-aml-workshop/elyra:0.0.1' --reference-policy=local --confirm
oc label is ml-workshop-elyra 'opendatahub.io/notebook-image=true'
```

Now it's time to test each of the tools installed. Each of the tools we use should have an OpenShift Route created, apart from Verta.ai, the model repository tool. So go ahead and create one for that:
```
oc expose svc ml-modeldb-webapp
```
## Test Routes
Then on the GUI, open the menu item _Networking->Routes_ and you'll see these routes:

![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/32-routes.png)

Test each route as follows:

- jenkins-ml-jenkins: login with your OpenShift credentials
- jupyterhub: login with your OpenShift credentials
- minio-ml-workshop: login with credentials _minio / minio123_
- ml-modeldb-webapp: no credentials needed
- odh-dashboard: not required for the workshop
- superset: login with credentials _admin / admin_

## Import assets

### Jenkins

Login to Jenkins as described previously and choose New Item as shown.
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/33-jenkins-new-item.png)

Name it _deploy-model_, select _Pipeline_ as shown and click *OK*:
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/34-new-item-deploy-model.png)

No go ahead and click _This project is parameterized_ and add the 2 String paramters _namespace_ (with default ml-workshop) and *experiment_id* as shown:
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/35-pipeline-param.png)

Don't save it yet.

Scroll down to the _Pipeline_ section. Inside the _Script_ box, paste the contents of [Jenkinsfile](https://raw.githubusercontent.com/masoodfaisal/ml-workshop/main/jenkins-pipeline/model/Jenkinsfile) as shown and click *Save*:

![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/36-add-jenkinsfile.png)

### Add raw CSV files to Minio S3 object storage

Login to Minio as described previously and choose the _rawdata_ bucket. Then drag the 2 files *Customer-Churn_P1.csv* and *Customer-Churn_P2.csv* to Minio ( located on your file system in $REPO_HOME/data ) as shown:

![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/37-drag-raw-files-to-minio.png)


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

- Install Jenkins Operator (this takes several minutes)
```
cd $REPO_HOME/helm/jenkins-operator
helm install ml-jenkins-operator .
```

- Install Open Data Hub Operator (this takes several minutes)
```
cd $REPO_HOME/helm/odh-operator
helm install ml-odh-operator .
```

At this point, on GUI go to Installed Operators and wait until both operators are installed

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

- Minio - our object stroage implemenation
```
cd $REPO_HOME/helm/minio
helm install ml-minio .
```

- Verta.ai - our model repository
```
cd $REPO_HOME/helm/modeldb
helm install ml-modeldb .
```

The next thing we need to do is install a custom Jupyter image that contains required libraries for the three data-science focused workshops. Run the following
```
cd $REPO_HOME/notebook-image
oc import-image ml-workshop-elyra --from='quay.io/ml-aml-workshop/elyra:0.0.1' --reference-policy=local --confirm
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

Login to Jenkins and choose New Item as shown.
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/33-jenkins-new-item.png)


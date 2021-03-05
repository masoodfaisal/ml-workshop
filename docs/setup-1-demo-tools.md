# Install the workshop tools
## Prerequisites
You'll need
- Helm, the Kubernetes package manager. It's available [here](https://helm.sh/docs/intro/install/)
- an OpenShift cluster - with admin rights. You can create one by following the instructions [here](http:/try.openshift.com)

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


- Install JENKINS OPERATOR
  (this takes several minutes)
```
cd $REPO_HOME/helm/jenkins-operator
helm install ml-jenkins-operator .
```




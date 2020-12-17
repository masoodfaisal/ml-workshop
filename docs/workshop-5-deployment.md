# OpenShift's ML/OPs deploys the model to production

## Introduction
In this sub-module, you'll get experience of OpenShift's CICD and ML/OPs capabilities to move the model we trained earler to a simulated production environment. In this way, you add speed and potentially quality and security to this deployment process.

This the right hand side section of the flow diagram depicts what's happening at this stage:


![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/22-FM-ML-Workshop-ml-ops.png)

## Instructions
If you haven't already, login to [Jenkins - for CICD and ML/OPs](https://jenkins-ml-jenkins-ml-workshop.apps.cluster-anz-ai-ml.rhtlabs.com/) using your OpenShift credentials, and accept the Authorisation prompt.


Choose New Item:


![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/23-jenkins-new-item.png)


Name your pipeline userXX-model-deploy - replacing the start with your USERNAME. Then click Pipeline, then click OK below:


![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/24-jenkins-name-choose-pipeline.png)


Then click _This Project is parameterised_ then _Add Parameter_ then _String Parameter_:


![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/24-jenkins-string-param1.png)


Then type _experiment_id_:


![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/24-jenkins-string-param2.png)


Now scroll down to the Pipeline section and insert the script in this repo at [jenkins-pipeline/model/Jenkinsfile](https://raw.githubusercontent.com/masoodfaisal/ml-workshop/main/jenkins-pipeline/model/Jenkinsfile) into that script box (copy and paste the script):











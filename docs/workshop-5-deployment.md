# OpenShift's ML/OPs deploys the model to production

## Introduction
In this sub-module, you'll get experience of OpenShift's CICD and ML/OPs capabilities to move the model we trained earler to a simulated production environment. In this way, you add speed and potentially quality and security to this deployment process.

This the right hand side section of the flow diagram depicts what's happening at this stage:


![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/22-FM-ML-Workshop-ml-ops.png)

## Instructions
If you haven't already, login to [Jenkins - for CICD and ML/OPs](https://jenkins-ml-jenkins-ml-workshop.apps.cluster-anz-ai-ml.rhtlabs.com/) using your OpenShift credentials, and accept the Authorisation prompt.


Once in Jenkins, select deploy-model -> down arrow -> Build with Parameters:
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/23-jenkins-run-params.png)


You'll be prompted for an experiment_id. To get this go to Minio -> Models and select the model with your USERNAME, in my case user29. Copy this value - without the trainling slash (in my case **customerchurnuser29162020200925297214**) 


![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/24-minio-experiment-id.png)



Now paste that value into experiment_id in Jenkins. Keep namespace as ml-workshop. Click Build:


![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/25-Pipeline deploy-model-success.png)



You'll see your pipeline run start on the left and after a few minutes you should see all green boxes indicating success.
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/26-pipeline-run-user29.png)


If it's unclear which pipeline is yours (if others are starting at the same time), drill into the #XX on the left under build history, and you'll see if it's yours 
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/26-pipeline-run-user29.png)






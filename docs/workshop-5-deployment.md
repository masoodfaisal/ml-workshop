# OpenShift's ML/OPs deploys the model to production

## Introduction
In this sub-module, you'll get experience of OpenShift's CICD and ML/OPs capabilities to move the model we trained earler to a simulated production environment. In this way, you add speed and potentially quality and security to this deployment process.

This the right hand side section of the flow diagram depicts what's happening at this stage:


![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/22-FM-ML-Workshop-ml-ops.png)

## Instructions
If you haven't already, login to [Jenkins - for CICD and ML/OPs](https://jenkins-ml-jenkins-ml-workshop.apps.cluster-anz-ai-ml.rhtlabs.com/) using your OpenShift credentials, and accept the Authorisation prompt.


Once in Jenkins, select deploy-model -> down arrow -> Build with Parameters:
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/23-jenkins-run-params.png)


You'll be prompted for an experiment_id. To get this go to Minio -> Models and select the model with your USERNAME, in my case user29. Copy this value - without the trailing slash (in my case **customerchurnuser29162020200925297214**) 


![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/24-minio-experiment-id.png)



Now paste that value into experiment_id in Jenkins. Keep namespace as ml-workshop. Click Build. You'll see your pipeline run start on the left and after a few minutes you should see all green boxes indicating success.
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/25-Pipelinedeploy-model-success.png)


If it's unclear which pipeline is yours (if others are starting at the same time), drill into the #XX on the left under build history, and you'll see if it's yours: 
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/26-pipeline-run-user29.png)


**NOTE: If you want to build the Explainer pipeline - so the reasons for model predictions are available, run the deploy-model-alibi in the same way**

----------------------------------------------------------------------

## Testing your model - making an inference API call.

Finally you can test you model that was deployed by Jenkins. I'm going to use [Postman - for my Model Serving/ Inference API call](https://www.postman.com/downloads) - but there are many other options.

Construct the API URL using your experiment_id you just used in Jenkins as follows:
```
https://${EXPERIMENT_ID}-ml-workshop.apps.{cluster URL}/api/v1.0/predictions
```
In my case it's
```
https://customerchurnuser29162020200925297214-ml-workshop.apps.cluster-anz-ai-ml.rhtlabs.com/api/v1.0/predictions
```

Next we need a sample payload representing the actual runtime data representing a customer whose probability of churning, we would like to assess.
To get such a sample payload, use [this JSON](https://raw.githubusercontent.com/masoodfaisal/ml-workshop/main/vegetta/payload.json)
Set your content to be JSON and click **Send**. You should get a successful response.


See my sample API call and succesful response:


![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/27-postman-call.png)



If you built the Explainer pipeline (deploy-model-alibi in Jenkins above), this can also be called in a similar way.
Just modify your API URL to the same as your main inference URL - with the **a-** prefix before your EXPERIMENT_ID:
```
https://a-${EXPERIMENT_ID}-ml-workshop.apps.{cluster URL}/api/v1.0/predictions

```


## Congratulations - you've completed the module!
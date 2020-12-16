# AI/ML on OpenShift - hands-on workshop

## Introduction
Today you'll follow a series of hands-on modules cover the end to end AI/ML workflow and lifcycle. The use case today will be predicting customer churn - though the capabilities and tools are transferrable to any AI/ML use case.

This diagram depicts the flow and actors involved at each stage:
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/1-ai-ml-workflow-diagram.png)

Today's workshop will be split up into sub-modules - logically following this workflow. 
- [Data Engineer prepares data](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/workshop-1-data-engineer.md)
- [Data Scientist visualises and analyses prepared data](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/workshop-2-data-science-visuals.md)
- [Data Scientist performs model experimentation](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/workshop-3-data-science-experiments.md)
- [Data Scientist trains best identified model](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/workshop-4-data-science-training.md)
- [Data Engineer prepares data](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/workshop-1-data-engineer.md)
- [OpenShift's ML/OPs deploys the model to production](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/workshop-5-deployment.md)


## Instructions
Your facilitator will have assigned you a username that you can use throughout today's workshop. In today's instructions 
- substitute your assigned username where you see **USERNAME**
- substitute your password (the same for everyone today) _openshift_ where you see **PASSWORD**

Now log into the various tools you'll be using today. Go ahead and accept any security warning as we're temporarily using a self-signed certificate. If prompted, use your **USERNAME** and **PASSWORD**:
- [OpenShift Console](https://console-openshift-console.apps.cluster-anz-ai-ml.rhtlabs.com)
- [Jupyter Notebooks](https://jupyterhub-ml-workshop.apps.cluster-anz-ai-ml.rhtlabs.com/). For more information on Jupyter see [jupyter.org](https://jupyter.org/).
- [Minio - our Object Storage implementaion](https://minio-ml-workshop-ml-workshop.apps.cluster-anz-ai-ml.rhtlabs.com). For **Access Key** use _minio_ and for **Secret Key** use _minio123_. With OpenShift, using shared object storage is an excellent means for collaboration, sharing of work and elimination of silos. For more information on Minio see [Minio Object Storage](https://min.io/).
- [Verta.ai](https://modeldb-ml-workshop.apps.cluster-anz-ai-ml.rhtlabs.com). Verta provides outstanding visualisation capabilities. For more see [verta.ai](https://www.verta.ai/)
- [Jenkins - for CICD and ML/OPs]()
- []()








After a short time later, the Service Mesh application and its components are installed. You can verify it on screen 
or in the command line as shown:
```
oc project istio-system
oc get pods -w
```

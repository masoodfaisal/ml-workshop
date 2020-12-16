# AI/ML on OpenShift - hands-on workshop

## Introduction
Today you'll follow a series of hands-on modules cover the end to end AI/ML workflow and lifcycle. The use case today will be predicting customer churn - though the capabilities and tools are transferrable to any AI/ML use case.

This diagram depicts the flow and actors involved at each stage:
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/1-ai-ml-workflow-diagram.png)

Today's workshop will be split up into sub-modules. 
- [Data Engineer prepares data](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/workshop-1-data-engineer.md)



## Instructions
Log into your OpenShift cluster ....








After a short time later, the Service Mesh application and its components are installed. You can verify it on screen 
or in the command line as shown:
```
oc project istio-system
oc get pods -w
```

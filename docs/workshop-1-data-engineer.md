# Data Engineer prepares data

## Introduction
In our first workshop sub-module the data engineer works in a dedicated Jupyter Notebook for combining 2 comma-separated-variable (CSV) files into a dataset that the data-scientist can conume to traing their models.

This diagram highlights the flow and actors involved at this Data Engineering stage:
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/2-FM-ML-Workshop-data-eng.png)

## Instructions
You should have already logged into [Jupyter Hub](https://jupyterhub-ml-workshop.apps.cluster-anz-ai-ml.rhtlabs.com/) on OpenShift. You should see a screen like this. Make the selections you see on screen and click Spawn:
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/2-data-engineer-jup-spawner.png)

Once in, you'll see a file list page. We need to clone this repository where your workshop files are downloaded from. To that click on New -> Terminal as shown
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/3-jup-new-terminal.png)


Once in the terminal clone the repository - which will pull it into your Jupyter Hub - and allow us open the notebooks:
```
git clone https://github.com/masoodfaisal/ml-workshop
```

Now go back to your file list page and you'll see the new folder you just cloned _ml-workshop_. Drill into notebook/ and open Merge_Data.ipynb

Now start to work your way through the notebook, reading docs and executing each individual cell in sequence  - by clicking in each cell and clicking Run as shown:


![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/4-jup-run-cell.png)

In the 5th cell, the one beginning with _*os.environ['PYSPARK_SUBMIT_ARGS']*_ modify _*spark.hadoop.fs.s3a.endpoint=http://172.30.97.178:9000*_ to the IP Address of your Minio Service. You'll find it under the OpenShift menu: _Networking->Services->Minio_ (your will be different)
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/28-minio-service.png)

This is a summary of what happens in the notebook (further details on the notebook itself):
- we install and import our desired libraries
- watermark our notebook - indicating which versions of which libraries we're using.
- build and start a Spark session. This may take a couple of minutes - this is your own dedicated Spark cluster - and it's quite resource hungry.
- pull in our two sets of raw data from Minio object storage
    - Customer-Churn_P1.csv
    - Customer-Churn_P2.csv
- join them using Spark and push them back to this location in Minio object storage under a location specific to your username
- **NOTE Before executing the last cell - be sure to change the user_id to your username**

![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/5-set-userid-data-eng-notebk.png)


Now close down your Merge_Data.ipynb notebook and move to the control panel - as shown. 
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/6-control-panel.png)

We need to shut Stop My server - because we'll need to spawn new images shortly as a Data Scientist:
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/7-shutdown-jup.png)


## Next Steps

Now move to the next section [Data Scientist visualises and analyses prepared data, experiments and trains model.](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/workshop-2-3-4-data-science.md)

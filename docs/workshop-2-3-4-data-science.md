# Data Scientist visualises and analyses prepared data, experiments and trains model.

## Introduction
In our second workshop sub-module the data scientist begins their work - also with a dedicated Jupyter Notebook. They analyse and visualise the data prepared by the data engineer in the previous step.

Then then exeriment with different training algorithms, _DecisionTreeClassifier_ and _RandomForestClassifier_, and picks the best one.

Then then train the model using their selected algorithem.

This diagram highlights the flow at this stage:
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/8-FM-ML-Workshop-visual.png)

## Instructions

In the last section, the data engieer's work, you pushed joined data to Object storage - as you can see in the diagram above. We need to take a record of the generated filename - as we'll be using it shortly. Move to your Minio tab (you opened it at the start) and navigate to Data -> data/full-data_csv**USERNAME** and copy this plus the name of the CSV-FILE, in my case **full_data_csvuser29/part-00000-59149e08-583c-46a5-bfa0-0b3abecbf1a3-c000.csv**. We'll refer to this is **CSV-FILE** below. As shown:
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/11-minio-prepared-csv-file.png)

## Data Scientist visualises and analyses the data

At the end of the previous section, you logged out of JupyterHub - and you should see a screen like this:
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/9-start-Jupyter.png)

Go ahead and start it up - and you'll again see the Spawn page - this time select the Data Science focused image, based on Elyra - which we built to save time and keep a consistent image across the organisation:
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/10-j-hub-spawner-elyra.png)

Once in, navigate to and open ml-workshop/notebook/Visulaise_Model.ipynb (You'll notice a different more modern user interface associated with this image). In the same way you did with the data engineer focused notebook _Merge_Data_, start to read the documentation on the notebook and run the individual cells as follows:
![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/12-run-new-Jupyter-interace.png)

On the third cell, beginning with _minioClient = get_s3_server()_, replace 




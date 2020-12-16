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


![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/12-run-new-jupy-interace.png)

On the third cell, beginning with _minioClient = get_s3_server()_, replace the filename in the second line, with your CSV-FILE you just retrieved in Minio:


![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/13-visualise-insert-file-name.png)

Continue to run your notebook to the end, cell by cell. You'll notice the various visual outputs you saw your instructor describe during the demo.

## Data Scientist experiments with different models

Now as a data scientist, we're going to run experiments with models based on 2 different algorithms, _DecisionTreeClassifier_ and _RandomForestClassifier_. We'll be assessing which os the better one, then we'll use that later to train the model that we'll push to production. As shown open up the notebook _Model_Experiments.ipynb_ and run the first 3 cells as far as and including the watermark cell.


![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/14-run-new-model-experiments.png)

You need to make a few changes to this notebook - specific to you as a user. First, on the 4th cell ( beginning with _dateTimeObj = datetime.now()_ ) change the name, inserting your USERNAME:


![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/15-model-experiments-experiment-name.png)

Run that cell.

The second user-specific change you'll need to make is on the next cell beginning with _minioClient = get_s3_server()_. In the same way you just did on the Visulaise_Model notebook, replace the filename in the second line, with your CSV-FILE:


![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/13-visualise-insert-file-name.png)

Continue to run your notebook, cell by cell. You'll notice similar outputs to your instructor's demo, initially building up and training using DecisionTreeClassifier.

When you get to this cell, prior to your RandomForestClassifier experiment, pause as you'll need to make the third user-specific change. In the same way you did earlier, change the experiment name to reflect your USERNAME:


![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/17-random-forest-model-experiment-name.png)


Continue to run the notebook, cell by cell to the end. The notebook will output the accuracy of the 2 experiments, using DecisionTreeClassifier and RandomForestClassifier. Keep a note of __accuracy__ and __ExperimentRun__ name, for both the DecisionTreeClassifier and RandomForestClassifier runs. E.g. see the accuracy of the RandomForestClassifier and its ExperimentRun:


![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/18-random-forest-accuracy-experiment-run.png)



## Data Scientist chooses and trains model

Our 2 experiments, using DecisionTreeClassifier and RandomForestClassifier didn't reveal hugely different accuracies - so we're going to use the DecisionTreeClassifier for performance reasons.

Open the Train_Model notebook and run the first 3 cell up to the watermark call as before:


![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/19-train-model.png)


Again as before, on the 4th cell ( beginning with _dateTimeObj = datetime.now()_ ) change the name, inserting your USERNAME:


![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/20-experiment-name.png)


Again, as before, on the next cell, beginning with _minioClient = get_s3_server()_, replace the filename in the second line, with the same CSV-FILE you substituted earlier:


![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/13-visualise-insert-file-name.png)


Continue to run the notebook, cell by cell to the end. You'll notice similar outputs to your instructor's. Finally the models are pushed to Minio Object storage, an effective workflow handoff mechanism.


Before we move to the next section, let's login to our Visualisation component [Verta](https://verta-ml-workshop.apps.cluster-anz-ai-ml.rhtlabs.com/). Navigate to Projects -> ml-workshop then drill into the customerchurnuser**XX** associated with your USERNAME as shown:


![](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/images/21-verta-1.png)


Now you'll see some very useful acccuracy and other stats, hyparameters and artifacts associated with each of your experiment runs - as you saw your instructor demonstrate.

## Next Steps

Now move to the final submodule [OpenShift's ML/OPs deploys the model to production](https://github.com/masoodfaisal/ml-workshop/blob/main/docs/workshop-5-deployment.md)
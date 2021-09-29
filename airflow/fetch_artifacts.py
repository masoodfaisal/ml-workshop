!pip install mlflow
!pip install minio
!pip install boto3
!pip install sklearn

import os
import mlflow
from minio import Minio

os.environ['MLFLOW_S3_ENDPOINT_URL']='http://minio-ml-workshop:9000'
os.environ['AWS_ACCESS_KEY_ID']='minio'
os.environ['AWS_SECRET_ACCESS_KEY']='minio123'
os.environ['AWS_REGION']='us-east-1'
os.environ['AWS_BUCKET_NAME']='mlflow'
os.environ['MODEL_NAME'] = 'rossdemo'
os.environ['MODEL_VERSION'] = '1'

HOST = "http://mlflow:5500"

model_name = os.environ["MODEL_NAME"]
model_version = os.environ["MODEL_VERSION"]

# model_name = "rossdemo"
# model_version = "1"

def get_s3_server():
    minioClient = Minio('minio-ml-workshop:9000',
                    access_key='minio',
                    secret_key='minio123',
                    secure=False)

    return minioClient

def init():
    mlflow.set_tracking_uri(HOST)
    print(HOST)
    # Set the experiment name...
    #mlflow_client = mlflow.tracking.MlflowClient(HOST)

def download_artifacts():
    print("loading mlflow model metadata...")
    model = mlflow.pyfunc.load_model(
        model_uri=f"models:/{model_name}/{model_version}"
    )

    print("initializing connection to s3 server...")
    minioClient = get_s3_server()

    #artifact_location = mlflow.get_experiment_by_name('ross-test').artifact_location
    run_id = model.metadata.run_id
    experiment_id = mlflow.get_run(run_id).info.experiment_id

    print("downloading artifacts...")
    #TODO replace the /3 with variable
    #print(f"{artifact_location}/{run_id}/artifacts/model/model.pkl")
    data_file_model = minioClient.fget_object("mlflow", f"/{experiment_id}/{run_id}/artifacts/model/model.pkl", "/tmp/model.pkl")
    data_file_requirements = minioClient.fget_object("mlflow", f"/{experiment_id}/{run_id}/artifacts/model/model.pkl", "/tmp/requirements.txt")
    #Using boto3 Download the files from mlflow, the file path is in the model meta
    #write the files to the file system
    print("download complete")

init()
download_artifacts()

from minio import Minio
from verta import Client
from minio.error import ResponseError
import os


def get_s3_server():
    minioClient = Minio('minio-ml-workshop:9000',
                        access_key='minio',
                        secret_key='minio123',
                        secure=False)

    return minioClient

def record_metrics(classifier, experiment_name, accuracy_score, hp):
    client = Client("http://chart-1603715522-webapp:3000")
    proj = client.set_project("ML Workshop")
    client.set_experiment("CutomerChrun-U001")
    run = client.set_experiment_run(experiment_name)

    for key, value in hp.items():
        run.log_hyperparameters({key : value})
    run.log_metric('accuracy', accuracy_score)
    run.log_tags([classifier])
    # TODO
    # run.log_dataset()
    # run.log_artifact_path()

def download_all_files(bucket_name):
    minioClient = get_s3_server()
    objects = minioClient.list_objects_v2(bucket_name=bucket_name,
                                          recursive=True)
    for obj in objects:
        print(obj.bucket_name, obj.object_name.encode('utf-8'), obj.last_modified,
              obj.etag, obj.size, obj.content_type)
        try:
            print(minioClient.fget_object(obj.bucket_name, obj.object_name,
                                          '/tmp/' + os.path.basename(obj.object_name)))
        except ResponseError as err:
            print(err)
import kfp
from kfp import dsl
from kfp.components import func_to_container_op, InputPath, OutputPath
from kfp import compiler
import kfp.notebook
import kfp.components as comp


@dsl.pipeline(
    name='Basic kfp Pipeline',
    description='Basic kfp Pipeline'
)
def sample_pipeline():
    data = dsl.ContainerOp(
        name='preprocess',
        image='fraud/scikit_pre_process:0.0.1') \
        .add_env_variable(k8s_client.V1EnvVar(name='MINIO_URL',
                                              value='http://minio-service.kubeflow.svc.cluster.local:9000')) \
        .add_env_variable(k8s_client.V1EnvVar(name='MINIO_KEY', value='minio')) \
        .add_env_variable(k8s_client.V1EnvVar(name='MINIO_SECRET', value='minio123'))

    # Train the model
    train = dsl.ContainerOp(
        name='trainmodel',
        image='fraud/scikit_train:0.0.1') \
        .add_env_variable(k8s_client.V1EnvVar(name='MINIO_URL',
                                              value='minio-service.kubeflow.svc.cluster.local:9000')) \
        .add_env_variable(k8s_client.V1EnvVar(name='MINIO_KEY', value='minio')) \
        .add_env_variable(k8s_client.V1EnvVar(name='MINIO_SECRET', value='minio123'))
    train.after(data)

    # Train the model
    validate = dsl.ContainerOp(
        name='validatemodel',
        image='fraud/scikit_validate:0.0.1') \
        .add_env_variable(k8s_client.V1EnvVar(name='MINIO_URL',
                                              value='minio-service.kubeflow.svc.cluster.local:9000')) \
        .add_env_variable(k8s_client.V1EnvVar(name='MINIO_KEY', value='minio')) \
        .add_env_variable(k8s_client.V1EnvVar(name='MINIO_SECRET', value='minio123'))
    validate.after(train)


compiler.Compiler().compile(sample_pipeline, 'samepl_pipeline.tar.gz')

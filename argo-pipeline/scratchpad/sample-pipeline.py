import kfp
from kfp import dsl
from kfp.components import func_to_container_op, InputPath, OutputPath
from kfp import compiler
import kfp.notebook
import kfp.components as comp

def python_image() -> str:
    return "python:3.7-slim"  

@func_to_container_op
def pre_process(train_location, test_location):
    '''Pre Process Data - For example check for NULL data in the set or we have a nuber for boolean column etc'''
    print(f'Print train and test location {train_location} {test_location}')
    # return kfp.dsl.ContainerOp(
    #     name='pre_process',
    #     image='basic_rhel_image'
    # )
    return 'success'

pre_process_op = comp.func_to_container_op(pre_process, base_image=python_image)




def train_model(train_location, test_location):
    '''Lets train the model and save it'''
    print(f'Train Model {train_location} {test_location}')
    return 'success'

train_model_op = comp.func_to_container_op(train_model, base_image=python_image)

# @func_to_container_op
def test_model(model_name, test_location):
    '''Validate the Model'''
    print(f'Validate Model {model_name} {test_location}')
    return 'success'
train_model_op = comp.func_to_container_op(test_model, base_image=python_image)


# @func_to_container_op
def deploy_model(a: float, b: float) -> float:
    '''Deploy Model'''
    return a + b
deploy_model_op = comp.func_to_container_op(deploy_model, base_image=python_image)    

@dsl.pipeline(
    name='Test Pipeline',
    description='Pipeline to show kube flow concepts'
)
def sample_pipeline(model_name='test'):
    pre_process_task = pre_process_op('1', model_name)
    train_task = train_model(train_model.output, model_name)


kfp.compiler.Compiler().compile(sample_pipeline, 'sample-pipeline.zip')
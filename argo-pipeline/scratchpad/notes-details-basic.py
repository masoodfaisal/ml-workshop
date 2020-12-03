import kfp

def pre_process(a: float, b: float) -> float:
    '''Pre Process Data'''
    return a + b

def train_model(a: float, b: float) -> float:
    '''Train Model'''
    return a + b

def test_model(a: float, b: float) -> float:
    '''Test Model'''
    return a + b

def deploy_model(a: float, b: float) -> float:
    '''Deploy Model'''
    return a + b

add_op = kfp.components.func_to_container_op(add)

from typing import NamedTuple
def my_divmod(dividend: float, divisor:float) -> \
       NamedTuple('MyDivmodOutput', [('quotient', float), ('remainder', float)]):
    '''Divides two numbers and calculate  the quotient and remainder'''
    #Imports inside a component function:
    import numpy as np

    #This function demonstrates how to use nested functions inside a
    # component function:
    def divmod_helper(dividend, divisor): 
	    return np.divmod(dividend, divisor)

    (quotient, remainder) = divmod_helper(dividend, divisor)

    from collections import namedtuple
    divmod_output = namedtuple('MyDivmodOutput', ['quotient', 'remainder'])
    return divmod_output(quotient, remainder)

divmod_op = kfp.components.func_to_container_op(
                my_divmod, base_image='tensorflow/tensorflow:1.14.0-py3')
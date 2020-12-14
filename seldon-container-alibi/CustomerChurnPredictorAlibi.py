import dill
from alibi.explainers import AnchorTabular
import numpy as np
import json
import pandas as pd

class CustomerChurnPredictorAlibi(object):

    def __init__(self):
        with open("CustomerChurnPredictorAlibi.dill", "rb") as x_f:
            self.explainer = dill.load(x_f)
        
    def predict(self, X, feature_names=None,  **kwargs):
        oned_X = X.flatten()
        oned_X = oned_X.astype(float)
        print(oned_X)
        total_values = len(oned_X)
        df = pd.DataFrame(x)
        df = df.values.reshape(3,)
        print(df.shape)
        print(df.values[0])
        print(df.values[1])
        explanation = self.explainer.explain(df.values[1])
        print("Predicted: " + str(explanation))
        return explanation['anchor']
        # return json.dumps(explanation, cls=NumpyEncoder)

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (
        np.int_, np.intc, np.intp, np.int8, np.int16, np.int32, np.int64, np.uint8, np.uint16, np.uint32, np.uint64)):
            return int(obj)
        elif isinstance(obj, (np.float_, np.float16, np.float32, np.float64)):
            return float(obj)
        elif isinstance(obj, (np.ndarray,)):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

x = [1.0, 2.0, 3.0]
print(len(x))
df = pd.DataFrame(x)
df = df.values.reshape(3,)
print('asdasd')
print(df.shape)

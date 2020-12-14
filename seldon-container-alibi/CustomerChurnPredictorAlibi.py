import dill
from alibi.explainers import AnchorTabular
import numpy as np
import json

class CustomerChurnPredictorAlibi(object):

    def __init__(self):
        with open("CustomerChurnPredictorAlibi.dill", "rb") as x_f:
            self.explainer = dill.load(x_f)
        
    def predict(self, X, feature_names=None,  **kwargs):
        print("Received: " + str(X))
        print("Received: " + str(X.flatten))
        explanation = self.explainer.explain(X.flatten)
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
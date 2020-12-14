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
        df = pd.DataFrame(oned_X)
        df = df.values.reshape(total_values,)
        print(df.shape)
        print(df)
        print(type(df))
        print(type(oned_X))
        try:
            explanation = self.explainer.explain(df, threshold=0.80)
        except:
            print('First Error')

        try:
            explanation = self.explainer.explain(oned_X, threshold=0.80)
        except:
            print('Second Error')
        print("Predicted: " + str(explanation))
        # return explanation['anchor']
        return json.dumps(explanation, cls=NumpyEncoder)

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



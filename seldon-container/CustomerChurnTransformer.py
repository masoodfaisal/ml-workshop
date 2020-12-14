import numpy as np
import joblib


class CustomerChurnTransformer(object):

    def __init__(self):
        self.encoder = joblib.load('CustomerChurnOrdinalEncoder.pkl')
        self.onehotencoder = joblib.load('CustomerChurnOneHotEncoder.pkl')

    def transform_input(self, X, feature_names, meta):
        print(X)
        print(feature_names)
        print(meta)
        X = self.encoder.transform(X)
        X = self.onehotencoder.transform(X)
        return X

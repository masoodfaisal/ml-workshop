import numpy as np
import joblib


class CustomerChurnTransformer(object):

    def __init__(self):
        self.encoder = joblib.load('CustomerChurnOrdinalEncoder.sav')
        self.onehotencoder = joblib.load('CustomerChurnOneHotEncoder.sav')

    def transform_input(self, X, feature_names):
        X = self.encoder.transform(X)
        X = self.onehotencoder.transform(X)
        return X

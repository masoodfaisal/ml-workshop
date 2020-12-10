import joblib


class CustomerChurnPredictor(object):

    def __init__(self):
        self.model = joblib.load('CustomerChurnPredictor.sav')

    def predict(self, X, features_names):
        return self.model.predict_proba(X)

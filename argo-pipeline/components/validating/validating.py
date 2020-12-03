import argparse
import argparse
import argparse
import numpy as np
import os
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def _validate(train_location, test_location):
    '''Pre Process Data - For example check for NULL data in the set or we have a nuber for boolean column etc'''
    print(f'Print train and test location {train_location} {test_location}')
    data = datasets.load_svmlight_file('/tmp/hdfc/data/validatedata')

    model = joblib.load('/tmp/hdfc/model/IrisClassifier.sav')
    result = model.score(data[0], data[1])
    print("Accuracy: %.2f%%" % (result*100.0))    

    return 'success'
     
if __name__ == '__main__':
     print('Validating data...')
     parser = argparse.ArgumentParser()
     parser.add_argument('--train_location')
     parser.add_argument('--test_location')
     args = parser.parse_args()
     _validate(args.train_location, args.test_location)     

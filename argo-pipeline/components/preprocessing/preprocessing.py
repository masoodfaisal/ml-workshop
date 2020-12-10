import argparse
import numpy as np
import os
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score



## may be these are public function so DS can use them while working on the notebooks
def _pre_process(train_location, test_location):
    '''Pre Process Data - For example check for NULL data in the set or we have a nuber for boolean column etc'''
    print(f'Print train and test location {train_location} {test_location}')
    print('Loading iris data set...')
    iris = datasets.load_iris()
    X, y = iris.data, iris.target
    X1, X2, y1, y2 = train_test_split(X, y, random_state=0, train_size=0.6)
    print('Dataset Splited!')
    datasets.dump_svmlight_file(X1, y1, '/tmp/xxx/data/traindata')
    datasets.dump_svmlight_file(X2, y2, '/tmp/xxx/data/validatedata')
    return 'success'
     
if __name__ == '__main__':
     print('Preprocessing data...')
     parser = argparse.ArgumentParser()
     parser.add_argument('--train_location')
     parser.add_argument('--test_location')
     args = parser.parse_args()
     _pre_process(args.train_location, args.test_location)
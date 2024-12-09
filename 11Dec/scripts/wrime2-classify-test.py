#!/usr/bin/env python3

import sys
import os
import json
import pickle
from tqdm import tqdm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, confusion_matrix
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-m", "--model", type=str, metavar="MODEL", required=True, help="Output model file")
parser.add_argument("input", type=str, metavar="FILE", help="Input file")
args = parser.parse_args()


with open(args.input, 'r') as rh:
    DATASET = json.load(rh)

with open(args.model, 'rb') as rh:
    model_pipeline = pickle.load(rh)

def extract_wrime2 (dataset, key='test'):
    _X_str = []
    _y = []

    if key not in dataset:
        raise RuntimeError ("ERROR: {key} is not found in the dataset.")
    else:
        # for data in tqdm(dataset[key]):
        #     _X_str.append (data["Sentence"].rstrip())
        #     if data["Writer_Sentiment"] > 0: _y.append(1)
        #     elif data["Writer_Sentiment"] < 0: _y.append(-1)
        #     else: _y.append(0)
        # print (f"Dataset {key} has been extracted.", file=sys.stderr)

        return _X_str, _y


# X_test_str, y_test = extract_wrime2(DATASET)
# y_predict = model_pipeline.predict(X_test_str)

# test_accuracy = accuracy_score(y_test, y_predict)
# print (f"Test accuracy: {100*test_accuracy:.3g} %")

# test_confusion_matrix = confusion_matrix(y_test, y_predict, labels=[-1, 0, 1])
# print (test_confusion_matrix)

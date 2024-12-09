#!/usr/bin/env python3

import sys
import os
import json
import pickle
from tqdm import tqdm

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from argparse import ArgumentParser

### コマンドライン引数・オプションのチェック
### argparse.ArgumentParserを使う
### ドキュメント https://docs.python.org/ja/3.6/howto/argparse.html
parser = ArgumentParser()
parser.add_argument("-b", "--binary", action="store_true", help="Use binary values for Bag-of-Words")
parser.add_argument("-m", "--model", type=str, metavar="FILE", required=True, help="Output model file")
parser.add_argument("input", type=str, metavar="FILE", help="Input file in JSON format")
args = parser.parse_args()

### モデルファイルが既に存在する場合はエラーとしてRuntimeError例外を送出
if os.path.exists(args.model):
    raise RuntimeError (f"ERROR: {args.model} already exists.")

### JSON形式で記録されたファイルを読み出す（train/dev/testすべてが入っていることに注意）
with open(args.input, 'r') as rh:
    DATASET = json.load(rh)


def extract_wrime2 (dataset, key='train'):
    """ JSON形式に変換された WRIME ver.2 のデータから文とラベルのリストを抽出する


    """
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


X_train_str, y_train = extract_wrime2(DATASET)
model_pipeline = make_pipeline(
        # CountVectorizer( binary=args.binary, ngram_range=(1,1), min_df=2 ),
        CountVectorizer(),
        LinearSVC(random_state=42, max_iter=3000)
        )

model_pipeline.fit(X_train_str, y_train)
train_accuracy = model_pipeline.score(X_train_str, y_train)

# X_dev_str, y_dev = extract_wrime2(DATASET, key='dev')
# dev_accuracy = model_pipeline.score(X_dev_str, y_dev)

# print (f"Training accuracy: {100*train_accuracy} %", file=sys.stderr)
# print (f"Dev accuracy: {100*dev_accuracy} %", file=sys.stderr)

with open(args.model, 'wb') as wh:
    pickle.dump(model_pipeline, wh)
    print (f"Success! The trained model has been saved into {args.model}.", file=sys.stderr)

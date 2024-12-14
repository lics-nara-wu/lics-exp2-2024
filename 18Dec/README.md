# 第11回 2024-12-18 (WIP)

## はじめに
須藤の担当回では日本語の自然言語処理に関わるプログラムの作成を通じて
- (1) 機械学習によるデータ分類（パターン認識）の基礎
- (2) [scikit-learn](https://github.com/scikit-learn/scikit-learn)を使った機械学習の基礎
- (3) 機械学習による日本語文書分類
- (4) 機械学習による日本語の分かち書き
を学びます。

第11回と第12回では (4) を行います。

## 実験環境
- G棟のLinuxを前提とします
- 実装言語はG棟のLinuxで標準利用可能な Python を基本とします
  - 自主的に他の言語で実装することは妨げませんが、scikit-learnと同じようにやるのはおそらくかなり大変です
  - ただし、データの前処理に係る部分はできるだけ提供している Python スクリプトを利用してください

> [!WARNING]
> ※ このPythonはバージョンが古いので、Pythonの最近の機能やライブラリがいろいろ使えません。
> G棟の環境で動くような仕組みで説明しますので、今どきの環境ではそのまま動かないかもしれませんがご容赦ください。

## Pythonのリファレンス
- [Python 3.6ドキュメント](https://docs.python.org/ja/3.6/)
- [Python 3.6標準ライブラリリファレンス](https://docs.python.org/ja/3.6/library/index.html)
- [本実験で使うPythonのライブラリ等の使い方説明](https://github.com/lics-nara-wu/lics-exp2-2024/edit/main/README_python.md)

> [!TIP]
> [Pythonの機能についての説明](https://github.com/lics-nara-wu/lics-exp2-2024/blob/main/README_python.md)にこの実験で使うPythonの機能の説明を記載します。
>
> 質問等で共有が必要になったときには随時更新します。

## 当日の実験の流れ
以下のような流れで進めます。自分で分かるという人はどんどん先に進めていただいてかまいません。

## 1. 実験の目的と内容
スライドを使って説明します。スライドはLMSで共有します。

## 2. Pythonの環境設定の呼び出し
[第10回での環境設定](https://github.com/lics-nara-wu/lics-exp2-2024/blob/main/11Dec/README.md)が終了しているものとして、それを呼び出します。
```
EXPDIR=${HOME}/exp2_2024_nlp
cd ${EXPDIR}
source ${EXPDIR}/.venv/bin/activate
```
`exp_2024_nlp` という仮想環境が有効になっていることを確認してください。
```
(exp2_2024_nlp) [sudoh@remote01 exp2_2024_nlp]$
```

## 3. 課題の技術的説明
スライドを使って説明します。スライドはLMSで共有します。

## 4. 今回の実験用データの前処理

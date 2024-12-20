# README_python.md
この実験で利用するPythonの機能等についての説明

## リストの操作
### リストの初期化
```
L = []
```

### リストへの要素の追加
```
L.append(1)
L.append(2)

L == [1, 2]
```

## ファイルの読み込み
テキストファイルを一行ごとに読み込むときは、読み込んだ結果に改行文字 (`\n`) がついてしまっているので、`rstrip`で除去する。
`rstrip`とは、文字列の右端にある指定した文字を取り去るためのメソッド。
```
with open(filename, 'r') as rh:
    for line in rh:
        line = line.rstrip("\n")
```

## argparse.ArgumentParser
コマンドライン引数・オプションを処理するためのライブラリ

標準的な使い方
```
parser = ArgumentParser()
parser.add_argument("-d", "--debug", action="store_true", help="debug mode")
parser.add_argument("-f", "--file", type=str, help="file")
parser.add_argument("-m", "--model", type=str, required=True, help="file")
parser.add_argument("input", type=str, help="input file")
args = parser.parse_args()
```
このように書くと、
- `args.debug`は実行時のコマンドラインオプションで`-d`もしくは`-debug`を指定した場合には`True`、そうでない場合には`False`が入る。
- `args.file`は実行時のコマンドラインオプションで`-f name.txt`もしくは`--file name.txt`を指定した場合には`name.txt`が入る。
- `args.model`は実行時のコマンドラインオプションで`-m name.model`もしくは`--model name.model`を指定した場合には`name.model`が入る。指定がない場合にはエラーを返す (`required=True`の効果)。
- `args.input`は実行時の引数で`name.txt`を指定した場合に`name.txt`が入る。指定がない場合にはエラーを返す。

例えば、上記の設定をしたプログラムであれば
```
python3 foo.py -d -f file1 -m file2 file3
```
を実行したとき
```
args.debug == True
args.file == file1
args.model == file2
args.input == file3
```
というようになる。

# use_spacy

## Overview
これは自然言語処理ライブラリであるspacyの機能をまとめたものです。

参考にしたサイトは以下のとおりです。

https://ishitonton.hatenablog.com/entry/2018/11/24/004748

## Description
### このパッケージの機能は以下のようになっています。
- extract_entity.py

→ （テキストから固有表現の抽出を行う）

- semantic_similarity.py

→ （入力された二つのテキストに対して意味的類似度（0-1の数値）を示す）

- similarity_value.py

→ （テキストに対して入力された単語と同じ品詞の意味的類似度を示す）

- spacy_preparation.py

→ （テキストをspacyで扱うための準備を行うもの）

  （テキストのインポートとトークン化を行う）

- split_sentence.py

→ （テキストの文章ごとの分割を行う）

- txt_pos.py

→ （テキストの品詞タグ付けを行う）

　（（テキスト, 品詞, 構文従属関係）のタプルを一つの要素とするリストの作成を行う）

- txt_token.py

→ （トークン化したテキストを単語ごとに分けるもの）
　
  （要素に分けてリストへの格納を行っている）

## How to build enviroment（環境を構築する方法）
- 

- 

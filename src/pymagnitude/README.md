# pymagnitude

## Overview
これはsp_ggiをpymagnitudeを利用して動かせるようにしたものです。

sp_ggiの詳細は以下のesaの記事を参照してください。

https://kithappyrobot.esa.io/posts/68

## Description
### このパッケージの機能は以下のようになっています。
- mg_sp_ggi

→ (pymagnitudeを利用してggiを動かすノードをまとめたもの)

- make_pkl

→ (ggiを動かすときに必要なpickleファイルを生成するプログラム)

- silent

→ (音声認識を使わずにもともと入力した文章でggiが正しく動作するか確認するためのプログラム)

- sp_ggi

→ (Ward2vecでggiを動かす)

- trash

→ (その他いろいろ確認するために作ったプログラム)

## How to build enviroment（環境を構築する方法）
- 基本的にはhappymimi_voiceのREADMEとか音声班のesaの記事を見てください

- pymagnitudeに関しては次のサイトを参考に

https://self-development.info/%E3%80%90python%E3%80%91%E7%88%86%E9%80%9F%E3%81%AE%E5%88%86%E6%95%A3%E8%A1%A8%E7%8F%BE%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AApymagnitude%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC/

- 使用したpymagnitudeのモデルは以下のリンクから

 https://github.com/plasticityai/magnitude
 
 →　Stanford - GloVe	Common Crawl 840B　の heavy を選ぶ（8Gくらい？）（プログラムのファイルのパス変えれば違うモデルでも多分大丈夫（？））
 
## Usage

### pickleファイルを作る
ggi_learning.py を実行する際にclass_by_mg.pkl(又はclass_by_word2vec.pkl)とclass_generalization.pklが必要になるため先に作っておく必要がある(pathは'~/catkin_ws/src/happymimi_voice/config')

- class_by_mg.py (class_by_word2vec.py), class_data_make.py　を実行する（pythonで動くのでrosrunしなくても良い）(最初はそこそこ時間がかかる)

### ggiを実行する

- happymimi_voice_common の tts_srvserver.py / stt_server.py を立てる

- ggi_learning.py と mg_test_phase.py を立てる (Word2vecで利用したいときはtest_phase.py)

- ggi_test.py　を実行　(ものと場所の登録が二回される、プログラムの中のggi_learningを呼び出す回数をいじれば変えられる)

### 音声認識を使わずにggiを実行する

- happymimi_voice_common の tts_srvserver.py / stt_server.py を立てる 

- ggi_learning_01.py ~ ggi_learning_03.py , test_phase_01.py を立てる 

  -> (文章を変えたいときはggi_learning_0~ の中のobject_name_00とかplase_name_00 , test_phase_01のstr_00を変える)
  
  -> (word2vecで作ったpickleファイルを使うときはggi_learning_01_00.py ~ を使う)

- ggi_test_01.py を実行　(ものと場所の登録が三回)

 ## EDITER
- 瓦　舜生(2021年度参加)
 
 
 
 
 
 

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------
# Title: sequence.txtをアノテーションするノード
# Author: Koya Okuse
#-----------------------------------------------------------

import os
import spacy

#sequence.txtの読み込み
file_path = '../../config/sequence_ex.txt'

#spacyのモデルの読み込み
nlp = spacy.load('en_core_web_sm')

#最終的にクラスにして呼び出す形にする
text = "Please escort {name} to the {location}, you will find him at the {location}"
sentence = ["none", "none", "none", "none"]
doc = nlp(text)
ch = False


def input_change(ch, input_sen, num):

    if ch:
        sentence.append(input_sen)

    else:
        sentence[num] = input_sen


# print([d for d in doc])
for d in doc:

    if d.text == "," :
        ch = True

    elif d.pos_ == "VERB" and d.dep_ != "aux":
        input_change(ch, d.text, 0)

    elif d.pos_ == "PRON" and d.dep_ == "pobj" or d.text == "name" or d.text == "category":
        input_change(ch, d.text, 1) 

    elif d.pos_ == "NOUN" and d.dep_ == "pobj" and d.text == "room" or d.text == "location":
        input_change(ch, d.text, 2)

print(sentence)


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
def read_input():
    text_cnt = 0
    result = ['none', 'none', 'none', 'none']
    #文章に"and"が存在した場合
    result_and = ['none', 'none', 'none', 'none']
    with open(file_path) as f:
        for sentence in f:
            #docはリスト化されている
            doc = nlp(sentence)
            for d in doc:
                if d.text == "," or d.text == "and":
                    text_cnt += 1
                if d.pos == "VERB":
                    result[0] = d.text

                elif d.text == "name":
                    result[2] = '{name}' 



def insert_output():

    with open(file_path) as f:
        new_sentence = f.readlines()

    new_sentence.insert(1, "output: example\n")

    with open(file_path, mode='r+') as f:
        f.writelines(new_sentence)

def insert_input():

    with open(file_path) as f:
        old_sentence = f.readline()

    with open(file_path, mode='r+') as f:
        new_sentence = "input: " + old_sentence 
        f.write(new_sentence)

def main():
    insert_input()
    insert_output()
    with open(file_path) as f:
        print(f.read())


if __name__ == '__main__':
    main()

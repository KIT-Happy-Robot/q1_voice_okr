#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
import spacy
from txt_pos import pos

nlp = spacy.load('en_core_web_sm')

def similarity(word):
    sim_list = []
    detail_list = []
    doc_w = nlp(u'' + word)
    for d_w in doc_w:
        detail_w = (d_w.text, d_w.pos_, d_w.dep_)
        detail_list.append(detail_w)
    doc = pos()
    for det_w in detail_list:
        for d in doc:
            if d[1] == det_w[1]:
                d0 = nlp(u'' + d[0])
                dw = nlp(u'' + det_w[0])
                sim_word = d0.similarity(dw)
                sim_list.append([det_w[0], d[0], sim_word])
    return sim_list

if __name__ == '__main__':
    word = input("英単語を一つ入力: ")
    print(similarity(word))
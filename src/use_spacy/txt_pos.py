#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
import spacy
from spacy_preparation import preparation

def pos(text):
    pos_list = []
    doc = preparation(text)
    for d in doc:
        pos_list.append((d.text, d.pos_, d.dep_))
    return pos_list

if __name__ == "__main__":
    text = input('英文を入力>> ')
    print(pos(text))

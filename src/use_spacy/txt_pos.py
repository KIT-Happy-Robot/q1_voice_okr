#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
from os import path
import spacy
from spacy_preparation import preparation

def pos():
    pos_list = []
    docs = preparation()
    for doc in docs:
        for d in doc:
            pos_list.append((d.text, d.pos_, d.dep_))
    return pos_list

if __name__ == "__main__":
    print(pos())

#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
from os import path
import spacy

nlp = spacy.load('en_core_web_sm')

file_path = path.expanduser("~/catkin_ws/src/q1_voice_okr/config/")

def pos():
    pos_list = []
    with open (file_path + "ex.txt", "r") as f:
        for text in f:
            text = text.replace("\n", "")
            doc = nlp(text)
            for d in doc:
                pos_list.append((d.text, d.pos_, d.dep_))
    return pos_list

if __name__ == "__main__":
    print(pos())

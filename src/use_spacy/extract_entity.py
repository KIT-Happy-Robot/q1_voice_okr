#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
import spacy
from os import path

nlp = spacy.load('en_core_web_sm')

file_path = path.expanduser("~/catkin_ws/src/q1_voice_okr/config/")

def okuse_koya():
    with open(file_path + "ex.txt", "r") as f:
        for text in f:
            text = text.replace("\n", "")
            doc = nlp(text)
            entity_list = ([(d.text, d.label_, spacy.explain(d.label_)) for d in doc.ents])
    return entity_list

if __name__ == "__main__":
    print(okuse_koya())

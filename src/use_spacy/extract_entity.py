#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
import spacy
from spacy_preparation import preparation

def extractEntity(text):
    doc = preparation(text)
    entity_list = ([(d.text, d.label_, spacy.explain(d.label_)) for d in doc.ents])
    return entity_list

if __name__ == "__main__":
    text = input("英文を入力>>")
    print(extractEntity(text))

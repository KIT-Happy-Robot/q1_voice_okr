#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
import spacy
from os import path
from spacy_preparation import preparation

def extractEntity():
    docs = preparation()
    for doc in docs:
        entity_list = ([(d.text, d.label_, spacy.explain(d.label_)) for d in doc.ents])
    return entity_list

if __name__ == "__main__":
    print(extractEntity())

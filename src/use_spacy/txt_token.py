#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
from os import path
import spacy
from spacy_preparation import preparation

def tokenText():
    sens = []
    docs = preparation()
    for doc in docs:
        word = [d for d in doc]
        sens.append(word)
    return sens

if __name__ == "__main__":
    print(tokenText())
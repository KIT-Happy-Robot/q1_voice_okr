#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
from os import path
import spacy
from spacy_preparation import preparation

def splitSentence():
    sens = []
    docs = preparation()
    for doc in docs:
        sents = list(doc.sents)
        for sent in sents:
            sens.append(sent)
    return (sens)

if __name__ == '__main__':
    print(splitSentence())

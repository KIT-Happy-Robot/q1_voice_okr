#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
import spacy
import pprint
from spacy_preparation import preparation

def splitSentence(text):
    sens = []
    doc = preparation(text)
    sents = list(doc.sents)
    for sent in sents:
        sens.append(sent)
    return (sens)

if __name__ == '__main__':
    text = input("英文を入力>> ")
    pprint.pprint(splitSentence(text))

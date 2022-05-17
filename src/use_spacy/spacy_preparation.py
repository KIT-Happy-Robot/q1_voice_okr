#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
import spacy

nlp = spacy.load('en_core_web_sm')

def preparation(text):
    doc = nlp(text)
    return doc

if __name__ == "__main__":
    text = input("英文を入力>> ")
    print(preparation(text))

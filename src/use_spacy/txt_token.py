#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
from os import path
import spacy
from spacy_preparation import preparation

def tokenText(text):
    doc = preparation(text)
    word = [d for d in doc]
    return word

if __name__ == "__main__":
    text = input("英文を入力>> ")
    print(tokenText(text))

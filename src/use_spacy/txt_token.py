#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
from os import path
import spacy
from spacy_preparation import preparation

def tokenText(text):
    sens = []
    doc = preparation(text)
    word = [d for d in doc]
    sens.append(word)
    return sens

if __name__ == "__main__":
    text = input("英文を入力>> ")
    print(tokenText(text))

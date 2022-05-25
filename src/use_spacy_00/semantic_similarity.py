#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
import spacy
from spacy_preparation import preparation

nlp = spacy.load('en_core_web_md')

def semeticSimilarity(word1, word2):
    word1 = preparation(word1)

    word2 = preparation(word2)

    word_similarity = word1.similarity(word2)

    return(word_similarity)

if __name__ == '__main__':
    word1 = input("英単語を入力>> ")
    word2 = input("英単語を入力>> ")
    print(semeticSimilarity(word1, word2))

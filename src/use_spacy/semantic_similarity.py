#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
import spacy

nlp = spacy.load('en_core_web_md')

def semeticSimilarity(word1, word2):
    word1 = nlp(word1)
    word2 = nlp(word2)

    word_similarity = word1.similarity(word2)

    return(word_similarity)

if __name__ == '__main__':
    print(semeticSimilarity('go', 'come'))

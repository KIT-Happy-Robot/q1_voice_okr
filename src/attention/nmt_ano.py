#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------
# Title: sequence.txtをアノテーションするノード
# Author: Koya Okuse
#-----------------------------------------------------------

import os
import spacy

file_path = '../../config/sequence_ex.txt'

def insert_output():

    with open(file_path) as f:
        new_sentence = f.readlines()

    new_sentence.insert(1, "output: example\n")

    with open(file_path, mode='r+') as f:
        f.writelines(new_sentence)

def insert_input():

    with open(file_path) as f:
        old_sentence = f.readline()

    with open(file_path, mode='r+') as f:
        new_sentence = "input: " + old_sentence 
        f.write(new_sentence)

def main():
    insert_input()
    insert_output()
    with open(file_path) as f:
        print(f.read())


if __name__ == '__main__':
    main()

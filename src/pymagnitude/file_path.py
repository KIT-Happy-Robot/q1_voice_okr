#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

file_path = os.path.expanduser('~/catkin_ws/src/voice_education/config/question_box.yaml')
with open(file_path,'r') as f:
    x = f.readlines()
    print(x)

file_path = ('test.txt')

with open(file_path,'r') as f:
    x = f.readlines()
    print(x)


print('getcwd:      ', os.getcwd())
print('__file__:    ', __file__)


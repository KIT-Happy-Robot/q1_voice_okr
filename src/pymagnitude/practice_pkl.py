#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import rospy
from os import path
import sys

file_path=path.expanduser('~/catkin_ws/src/happymimi_voice/config/')

with open(file_path+'object_file.pkl','rb') as f:
    print(pickle.load(f))

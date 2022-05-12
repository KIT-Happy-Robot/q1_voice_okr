#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os.path
import rospy
import pickle

file_path=os.path.expanduser('~/catkin_ws/src/happymimi_voice/config')
with open(file_path+"/class_generalization.pkl","wb") as f:
    

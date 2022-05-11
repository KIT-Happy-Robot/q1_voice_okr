#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from happymimi_voice_msgs.srv import GgiLearning
from happymimi_voice_msgs.srv import GgiLearningResponse
import pprint

test_phase_01 = rospy.ServiceProxy('/ggi_learning',GgiLearning)

ser_01 = str(test_phase_01())

pprint.pprint(ser_01)

test_phase_02 = rospy.ServiceProxy('/ggi_learning_02',GgiLearning)

ser_02 = str(test_phase_02())

pprint.pprint(ser_02)

test_phase_03 = rospy.ServiceProxy('/ggi_learning_03',GgiLearning)

ser_03 = str(test_phase_03())

pprint.pprint(ser_03)

while 1:

    test_phase_01 = rospy.ServiceProxy('/test_phase',GgiLearning)

    ser_01 = bool(test_phase_01())

    if ser_01:

        pprint.pprint(ser_01)
        break




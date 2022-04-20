#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from happymimi_voice_msgs.srv import GgiLearning
from happymimi_voice_msgs.srv import GgiLearningResponse
import pprint

test_phase_00 = rospy.ServiceProxy('/ggi_learning',GgiLearning)

ser_00 = str(test_phase_00())

pprint.pprint(test_phase_00)

test_phase_01 = rospy.ServiceProxy('/test_phase',GgiLearning)


ser_01 = str(test_phase_01())


pprint.pprint(test_phase_01)




#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import rospy
import roslib
import time
import sys 
import smach
import smach_ros
from std_msgs.msg import String, Float64
from geometry_msgs.msg import Twist
from happymimi_msgs.srv import StrTrg
from happymimi_voice_msgs.srv import YesNo
from happymimi_navigation.srv import NaviLocation
base_path = roslib.packages.get_pkg_dir('happymimi_teleop') + '/src/'
sys.path.insert(0, base_path)
from base_control import BaseControl


from happymimi_voice_msgs.srv import GgiLearning
from happymimi_voice_msgs.srv import GgiLearningResponse


tts_pub = rospy.ServiceProxy('/tts', StrTrg)

test_phase_00 = rospy.ServiceProxy('/ggi_learning',GgiLearning)


class ():#
    




class ():#



class ():#



class ():#   



if __name__ == '__main__':
    rospy.init_name('bf/ggi_master')
    rospy.loginfo('Start sp_ggi')
    tts_pub("Start sp_ggi")
    sm_top = smach.StateMachine(outcomes = ["finish_sm_top"])
    with sm_top:
        smach.StateMachine.add('',  ,
                transitions = {'find_success':'GRASP_OR_PASS',
                               'find_failure':'FIND_BAG'},
                remapping = {'find_angle_in':'find_angle',
                             'find_angle_out':'find_angle'})



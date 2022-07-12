#/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import roslib
import time
import sys
import smach
import smach_ros
from std_msgs.msg import String, Float64
#from geometry_msgs.msg import Twist
from happymimi_msgs.srv import StrTrg
from happymimi_voice_msgs.srv import YesNo
#from happymimi_navigation.srv import NaviLocation
#base_path = roslib.packages.get_pkg_dir('happymimi_teleop') + '/src/'
#sys.path.insert(0, base_path)
#from base_control import BaseControla
from happymimi_navigation.srv import SetLocation

from enter_room.srv import EnterRoom

from happymimi_voice_msgs.srv import GgiLearning
from happymimi_voice_msgs.srv import GgiLearningResponse


tts_pub = rospy.ServiceProxy('/tts', StrTrg)
stt_pub = rospy.ServiceProxy('/stt_server', SpeechToText)

test_phase_00 = rospy.ServiceProxy('/ggi_learning',GgiLearning)

#Traning_Phase
class Move_First(smach.State):#初期位置まで移動
    def __init__(self):
        smach.State.__init__(self, outcomes = ['move_first_finish'])

    def execute(self, state):
        rospy.loginfo('Executing state: MOVE_FIRST')
        enter_room = rospy.ServiceProxy('/enter_room_server', EnterRoom)
        enter_room(1.0, 0.5)
        return 'move_first_finish'

class Chaser (smach.State):#物体がある位置まで移動
    def __init__(self):
        smach.State.__init__(self, outcomes = ['chaser_finish'],
                                   input_keys = ['PASS_count_in'],
                                   output_keys = ['PASS_count_out'])
        self.chaser_pub = rospy.Publisher('/follow_human', String, queue_size = 1)
        rospy.Subscriber('/find_str', String, self.findCB)
        rospy.Subscriber('/cmd_vel', Twist, self.cmdCB)
        self.yesno_srv = rospy.ServiceProxy('/yes_no', YesNo)
        self.base_control = BaseControl()
        self.find_msg = 'NULL'
        self.cmd_sub = 0.0
        self.start_time = time.time()

    def findCB(self, receive_msg):
        self.find_msg = receive_msg.data

    def cmdCB(self, receive_msg):
        self.cmd_sub = receive_msg.linear.x

    def execute(self, state):
        rospy.loginfo('Executing state: CHASER')
        pass_count - userdata.PASS_count_in
        tts_pub = "I'll follow you."
        self.chaser_pub.publish('start')
        while not rospy.is_shutdown():
            rospy.sleep(0.1)
            now_time = time.time() - self.find_time
            if self.cmd_sub == 0.0 and self.find_msg == 'NULL':
                self.find_msg = 'lost_stop'
                self.strat_time = time.time()
            elif self.cmd_sub == 0.0 and self.find_msg == 'NULL':
                tts_pub('Is this the location of the object')
                count = False
                while count:
                    ans = stt_pub(short_str = True,
                                  context_phrases = ["yes","no"]).result_str
                    if ans in "yes":
                        self.chaser_pub.publish('stop')
                        self.base_control.rotateAngle(0, 0)
                        userdata.PASS_count_out = pass_count + 1
                        return 'chaser_finish'
                    elif ans in "no":
                        tts_pub = ("OK, continue to follow")
                        count = True
                    else:
                        continue
                continue
            elif self.find_msg == "lost":
                self.strat_time == time.time()
                self.find_msg ="lost_after"
            elif self.find_msg == "lost_after" and now_time >= 1.0:
                tts_pub("I lost sight of you. Wait for me please")
                self.find_msg = "lost_long"
            elif self.find_msg == "lost_long" and now_time >= 11.0:
                tts_pub('Is this the location of the object')
                count = False
                while count:
                    ans = stt_pub(short_str = True,
                                  context_phrases = ["yes","no"]).result_str
                    if ans == "yes":
                        self.chaser_pub.publish('stop')
                        self.base_control.rotateAngle(0, 0)
                        userdata.PASS_count_out = pass_count + 1
                        return 'chaser_finish'
                    elif ans == "no":
                        tts_pub = ("OK, continue to follow")
                        self.find_msg = "NULL"
                        count = True
                    else:
                        continue
            elif self.cmd_sub != 0.0:
                seld.find_msg = "NULL"
            else:
                pass

class Register (smach.State):#場所と物の登録
    def __init__(self):
        smach.State.__init__(self, outcomes = ['register_success',
                                               'register_failure',
                                               'finish_traning'],
                                    input_keys = ['count_in'],
                                    output_keys = ['count_out'])
        self.learning = rospy.ServiceProxy('/ggi_learning',GgiLearning)

    def execute(self, userdata):
        count = userdata.count_in
        rospy.loginfo('Executing state: REGISTER')
        plase =  self.learning().split('"')
        plase_name = plase[1]
        if plase_name:
            if count < 2:
                count += 1
                userdata.count_out = count
                self.set = rospy.ServiceProxy('/set_location', SetLocation)
                self.set("state: 'add' name: {}".format(plase_name))
                if count == 2:
                    self.save = rospy.ServiceProxy('/set_location', SetLocation)
                    self.save(("state: 'save' name: 'ggi_location.yaml'")
                return 'register_success'
            else:
                return 'finish_traning'
        else:
            return 'register_failure'

#Test_Phase

class Get_Plase(smach.State):#命令文を読み解く
    def __init__(self):
        smach.State.__init__(self, outcomes = ['get_plase_success'],
                                   input_keys = [''],
                                   output_keys = [''])
        self.a = rospy.ServiceProxy('test_phase',GgiLearning)
    def execute(self, state):
        rospy.loginfo('Executing state: GET_PLASE')
        self.a()
        return 'get_plase_success'


class Get_Object(smach.State):#物体がある場所まで移動して掴む
    def __init__(self):
        smach.State.__init__(self, outcomes = ['get_object_success',
                                               'get_object_failure'])
    def execute(self, state):
        rospy.loginfo('Executing state:GET_OBJECT')
        if True:
            return 'get_object_success'
        else:
            return 'get_object_failure'

class Return(smach.State):#オペレーターの位置まで帰る
    def __init__(self):
        smach.State.__init__(self, outcomes = ['return_finish',
                                               'ggi_finish'],
                                    input_keys = ['count_in'],
                                    output_keys = ['count_out'])

    def execute(self, userdata):
        count = userdata.count_in
        if count < 4:
            count += 1
            userdata.count_out = count
            return 'return_finish'
        else:
            tts_pub('Finish go get it. Thank you very much.')
            return 'ggi_finish'




if __name__ == '__main__':
    rospy.init_node('ggi_master')
    rospy.loginfo('Start sp_ggi')
    tts_pub("Start go get it")
    sm_top = smach.StateMachine(outcomes = ["finish_sm_top"])
    sm_top.userdata.count = 0
    with sm_top:

        smach.StateMachine.add(
                'MOVE_FIRST',
                Move_First(),
                transitions = {'move_first_finish':'CHASER'},
                remapping = {'count_in':'count',
                             'count_out':'count'})



        smach.StateMachine.add(
                'CHASER',
                Chaser(),
                transitions = {'chaser_finish':'REGISTER'},
                remapping = {'PASS_count_in':'GOP_count',
                             'PASS_count_out':'GOP_count'})

        smach.StateMachine.add(
                'REGISTER',
                Register(),
                transitions = {'register_success':'CHASER',
                    'register_failure':'REGISTER',
                               'finish_traning':'GET_PLASE'},
                remapping = {'count_in':'count',
                             'count_out':'count'})

        smach.StateMachine.add(
                'GET_PLASE',
                Get_Plase(),
                transitions = {'get_plase_success':'GET_OBJECT'},
                remapping = {'':'',
                             '':''})

        smach.StateMachine.add(
                'GET_OBJECT',
                Get_Object(),
                transitions = {'get_object_success':'RETURN',
                               'get_object_failure':'GET_OBJECT'},
                remapping = {'':'',
                             '':''})

        smach.StateMachine.add(
                'RETURN',
                Return(),
                transitions = {'return_finish':'GET_PLASE',
                               'ggi_finish':'finish_sm_top'},
                remapping = {'count_in':'count',
                             'count_out':'count'})


        outcomes = sm_top.execute()

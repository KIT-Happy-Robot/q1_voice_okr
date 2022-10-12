#usr/bin/env python
# -*- coding: utf-8 -*-

import os
import rospy
import randam
from happymimi_msgs.srv import StrTrg
from happymimi_voice_msgs.srv import SpeechToText

file_path = os.path.expanduser("~/catkin_ws/src/")
path = os.path.expanduser('~/catkin_ws/src/happymimi_voice/config')
pos_tag = StanfordPOSTagger(model_filename = path +
                        "/dataset/stanford-postagger/models/english-bidirectional-distsim.tagger",
                        path_to_jar = path + "/dataset/stanford-postagger/stanford-postagger.jar")

class FmmStruction:
    def __init__(self):
        rospy.loginfo("Waiting for stt and tts")
        rospy.wait_for_service('/tts')
        rospy.wait_for_service('/stt_server')
        stt_pub = rospy.ServiceProxy('/stt_server', SpeechToText)
        tts_pub = rospy.ServiceProxy('/tts_srvserver', StrTrg)
        rospy.loginfo("server is ready")
        self.server=rospy.Service('/fmm_character',srv,self.main)
        self.features = ["clothing","age","height","gender","skin color","hair color"]
        self.feature_dic = {"clothing":"",
                            "age":"How old are you",
                            "height":"how tall are you",
                            "gender":"Cloud you tell me your gender",
                            "skin color":"what is your skin color",
                            "hair color":"what is your heir color"}

    def main(_dammy):







    def get_fiatuer():
        with open(file_path + "/q1_voice_okr/config/")
            question = feature_dic.get(featuer)
                if question:
                    tts_pub(question)
                    ans = stt_pub(context_phrases = ["",],boost_value = 0).result_str
                    pos=pos_tag.tag(ans.split())
                    if feature == "clothing":


                    elif feature == "age":

                    elif feature == "height":

                    elif feature == "gender":

                    elif feature == "skin color":

                    elif feature == "heir color":

            else:
                return False





if __name__ == '__main__':
    rospy.init_node('fmm_character')
    FmmStruction()
    rospy.spin()


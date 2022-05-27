#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import roslib
import wdys_def
from happymimi_voice_msgs.srv import WhatDidYouSay
from happymimi_voice_msgs.srv import WhatDidYouSayResponse

from happymimi_voice_msgs.srv import SpeechToText
from happymimi_voice_msgs.srv import SpeechToTextResponse
from happymimi_voice_msgs.srv import TTS
from happymimi_voice_msgs.srv import TTSResponse

from happymimi_msgs.srv import StrTrg



tts_pub = rospy.ServiceProxy('/tts', StrTrg)
stt_pub = rospy.ServiceProxy('/stt_server', SpeechToText)


def main():
    
    while 1:
        tts_pub("Are you ready")
        print("Are you ready")
        sen = stt_pub(short_str = True).result_str

        if sen == "yes":
            break

    count = 0
    while count != 10:
        tts_pub("Talk to me")
        print("Ready")
        service = rospy.ServiceProxy('/bf/wdys_sub',WhatDidYouSay)
        ser = service().result
        if  ser:
            count += 1
            print(count)
        else:
            tts_pub("Sorry I couldn't be recognized")
            print("one more time")
            
            






if __name__ == '__main__':
    rospy.init_node('wdys_main')
    main()          

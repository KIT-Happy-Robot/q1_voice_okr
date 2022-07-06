#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import roslib

from happymimi_voice_msgs.srv import WhatDidYouSay
from happymimi_voice_msgs.srv import WhatDidYouSayResponse
from happymimi_voice_msgs.srv import SpeechToText
from happymimi_voice_msgs.srv import SpeechToTextResponse
from happymimi_voice_msgs.srv import TTS
from happymimi_voice_msgs.srv import TTSResponse
from happymimi_msgs.srv import StrTrg
tts_pub = rospy.ServiceProxy('/tts', StrTrg)
stt_pub = rospy.ServiceProxy('/stt_server', SpeechToText)


tts_pub("こんにちわ")
sen = stt_pub(short_str = True).result_str
print(sen)

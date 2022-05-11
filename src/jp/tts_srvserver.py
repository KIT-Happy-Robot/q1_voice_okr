#!/usr/bin/env python
#-*- coding: utf-8 -*-
#[tts_stdserver.py]

import roslib
import rospy
#from happymimi_voice_msgs.srv import TTS, TTSResponse
from happymimi_msgs.srv import StrTrg,StrTrgResponse
from google.cloud import texttospeech

import wave
import pyaudio

Filename = 'output.wav'

class TTS_server(object):
    def __init__(self):
        rospy.init_node('common_texttospeech')
        self.srv = rospy.Service('/tts', StrTrg, self.execute)
        rospy.loginfo("Ready to tts stdserver")
        rospy.spin()

    def execute(self, data):
        client = texttospeech.TextToSpeechClient()
        synthesis_input = texttospeech.SynthesisInput(text=data.data)
        voice = texttospeech.VoiceSelectionParams(
            language_code='ja-JP',
            name='ja-JP-Standard-A',
            #ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
            )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16)

        response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

        with open(Filename, 'wb') as out:
            out.write(response.audio_content)
            print('Audio content written to file ' + Filename)

        self.PlayWaveFile()
        return StrTrgResponse()

    def PlayWaveFile(self):
        try:
            wf = wave.open(Filename, "rb")
            print("Time[s]:", float(wf.getnframes()) / wf.getframerate())
        except FileNotFoundError:
            print("[Error 404] No such file or directory: " + Filename)
            return

        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        chunk = 1024
        data = wf.readframes(chunk)
        while data != b'':
            stream.write(data)
            data = wf.readframes(chunk)
        stream.stop_stream()
        stream.close()
        wf.close()
        p.terminate()
        return


if __name__ == '__main__':
    TTS_server()
    rospy.spin()

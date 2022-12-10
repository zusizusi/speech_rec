#!/usr/bin/env python3
import rospy
from std_srvs.srv import SetBool, SetBoolResponse
import speech_recognition as sr


def listen_voice():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            voice_text = listener.recognize_google(voice)
            print(voice_text)
            return voice_text
    except:
        print("sorry I could not listen")
        return "failed"


def callback_srv(data):
    resp = SetBoolResponse()
    if data.data == True:
        voice = listen_voice()
        resp.message = voice
        resp.success = True
    else:
        resp.message = "Failed"
        resp.success = False
    print(resp.message)
    return resp


if __name__ == "__main__":
    rospy.init_node("srv_server")
    srv = rospy.Service("speech_rec", SetBool, callback_srv)
    print("ready")
    rospy.spin()

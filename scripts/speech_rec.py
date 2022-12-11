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
            if "apple" in voice_text or "Apple" in voice_text:
                return "apple", True
            elif "ball" in voice_text or "Ball" in voice_text:
                return "ball", True
            elif "orange" in voice_text or "Orange" in voice_text:
                return "orange", True
            else:
                return voice_text, False
    except:
        print("sorry I could not listen")
        return "failed", False


def callback_srv(data):
    resp = SetBoolResponse()
    if data.data == True:
        voice, success_flag = listen_voice()
        if success_flag is True:
            resp.message = voice
            resp.success = True
        else:
            resp.message = voice
            resp.success = False

    else:
        resp.message = ""
        resp.success = False
    print(resp.message)
    return resp


if __name__ == "__main__":
    rospy.init_node("srv_server")
    srv = rospy.Service("speech_rec", SetBool, callback_srv)
    print("ready")
    rospy.spin()

import speech_recognition as sr

listener = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
        voice_text = listener.recognize_google(voice)
        print(voice_text)
except:
    print('sorry I could not listen')
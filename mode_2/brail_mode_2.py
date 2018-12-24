#Python 2.x program to transcribe an Audio file
import speech_recognition as sr
import os
import time
from solenoid import instrument
while True:
    print 'start recording'
    os.system("arecord -d 3 -D plughw:1,0 test.wav")
    print 'recoding done'


    AUDIO_FILE = ("test.wav")
    r = sr.Recognizer()

    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  

    #e f h j n  o r u y
    try:
        k=r.recognize_google(audio)
        instrument(k)
        print("The audio file contains: " + k)
     
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        #break
     
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        #break

    




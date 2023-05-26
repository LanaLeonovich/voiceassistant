# Kesha 1.0
import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime

# settings
opts = {
    "alias": ('Keshun', 'Kush', 'Kesh', 'Kesha'),
    "tbr": ('tell', 'show', 'how', 'speak'),
    "cmds": {
        "ctime": ('time', 'time now', 'whats the time'),
        "radio": ('play the music', 'play radio', 'open radio'),
        "stupid1": ('tell me the jike', 'make me laugh', 'do you know jokes')
    }
}


# functions
def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="en-EN").lower()
        print("[log] Recognised: " + voice)

        if voice.startswith(opts["alias"]):
            # talking to kesha
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()

            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

            # doing the command
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print("[log] Your voice was not recognised!")
    except sr.RequestError as e:
        print("[log] Unknown trouble, check the internet connection!")


def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt

    return RC


def execute_cmd(cmd):
    if cmd == 'ctime':
        # telling the time
        now = datetime.datetime.now()
        speak("Now " + str(now.hour) + ":" + str(now.minute))

    elif cmd == 'radio':
        # playing radio
        os.system("D:\\Jarvis\\res\\radio_record.m3u")

    elif cmd == 'stupid1':
        # telling the joke
        speak("My programmer did not teach me to joke ... Ха ха ха")

    else:
        print('Command was not recognized!')


# starting
r = sr.Recognizer()
m = sr.Microphone(device_index=1)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

# Only if zou have voices
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[4].id)

# forced cmd test
speak("Can not tell you joke yet ... Hа Hа Hа")

speak("Hello, my friend")
speak("Kesha is listening...")

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1) # infinity loop
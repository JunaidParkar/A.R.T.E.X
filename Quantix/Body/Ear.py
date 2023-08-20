import sys
import os
sys.path.append(os.environ.get('Quantix'))
import speech_recognition as sr
from googletrans import Translator
import json
import Quantix.Brain.Paths as fp
from Quantix.Body.Hand import printSimple, printData

def hear():
    try:
        with open(fp.LOCALDATA_CONFIG_FILE, "r") as f:
            micConfig = json.load(f)['microphone']
            r = sr.Recognizer()
            with sr.Microphone() as source:
                printData("Listening....")
                r.adjust_for_ambient_noise(source)
                r.pause_threshold = micConfig['pause_treshold']
                audio = r.listen(source, micConfig['min_listen_timer'], micConfig['max__listen_timer'])
            try:
                printData("Recognizing...")
                query = r.recognize_google(audio, language='en')
            except :
                return ""
            f.close()
            return str(query).lower()
    except:
        printData("Error: Unable to load configuration file...")

def listen() :
    query = hear()
    printSimple(f"Your Command : {query}\n")
    return query
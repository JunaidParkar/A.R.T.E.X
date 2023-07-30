# import sys
# import os

# sys.path.append(os.environ.get('Zubia'))


import speech_recognition as sr
from googletrans import Translator
import json
import Zubia.Brain.Paths as fp

def hear():
    try:
        with open(fp.LOCALDATA_CONFIG_FILE, "r") as f:
            micConfig = json.load(f)['microphone']
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening....")
                r.adjust_for_ambient_noise(source)
                r.pause_threshold = micConfig['pause_treshold']
                audio = r.listen(source, micConfig['min_listen_timer'], micConfig['max__listen_timer'])
            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language='hi-In')
            except :
                return ""
            f.close()
            return str(query).lower()
    except:
        print("Unable to load configuration file...")
        
def translateToEnglish(text):
    try:
        translate = Translator()
        result = translate.translate(str(text), 'en')
        data = result.text
        return data
    except:
        return ""
    
def listen() :
    query = hear()
    data = translateToEnglish(query)
    print(f"Your Command : {data}\n")
    return data
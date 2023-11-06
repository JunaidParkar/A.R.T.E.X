import sys
import os
sys.path.append(os.environ.get('EvoAI'))
import pyttsx3
import json
from Fun.Body.Hand import printData
from Fun.Brain.Paths import LOCALDATA_CONFIG_FILE

def speak(text: str):
    try:
        with open(LOCALDATA_CONFIG_FILE) as f:
            voiceConfig = json.load(f)['voice']
            engine = pyttsx3.init()
            voices = engine.getProperty("voices")
            voice_index = voiceConfig['index']
            voice_id = voices[voice_index].id
            engine.setProperty("voice", voice_id)
            engine.setProperty("rate", voiceConfig['rate'])
            printData(text)
            engine.say(text)    
            engine.runAndWait()
    except Exception as e:
        printData(f"Unable to load configuration file... ${e}")
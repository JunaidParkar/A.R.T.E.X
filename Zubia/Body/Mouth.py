import sys
import os

sys.path.append(os.environ.get('Zubia'))

import pyttsx3
import json
from Zubia.Body.Hand import printData
import Zubia.Brain.Paths as fp

def speak(text):
    try:
        with open(fp.LOCALDATA_CONFIG_FILE) as f:
            voiceConfig = json.load(f)['voice']
            engine = pyttsx3.init()
            voices = engine.getProperty("voices")
            try:
                voice_index = voiceConfig['index']
                if voice_index < 0 or voice_index >= len(voices):
                    print("Invalid voice index. Re-configure index of voice in config.json")
                elif voices[voiceConfig['index']].name.lower() != "Microsoft Zira Desktop - English (United States)".lower():
                    print("Voice mis-matched ")
                elif voices[voiceConfig['index']].name.lower() == "Microsoft Zira Desktop - English (United States)".lower():
                    voice_id = voices[voice_index].id
                    engine.setProperty("voice", voice_id)
                    engine.setProperty("rate", voiceConfig['rate'])
                    printData(f"Zubia: {text}")
                    engine.say(text)
                    engine.runAndWait()
                else: 
                    print("Unknown error occured")
            except (KeyError, ValueError) as e:
                print("Error: Invalid voice configuration.")
    except:
        print("Unable to load configuration file...")
import os
import sys
os.system("cls" if os.name == "nt" else "clear")
os.system('title Evo AI Reminder 2.0.0')
import time
import os
import sys
import datetime
import pyttsx3
import pickle
import json
sys.path.append(os.environ.get('EvoAI'))
from Evo.Brain.Paths import TEMP_FOLDER, PRIVATE_4, LOCALDATA_CONFIG_FILE
print("fl imp")

def printData(data: str):
    print("")
    print(f"Evo: {data}")

def rmpt():
    pvt = os.path.join(os.path.split(TEMP_FOLDER)[0], "Brain", "Datasets", ".private")
    fl = os.path.join(pvt, PRIVATE_4)
    return fl

def loadReminder():
    try:
        with open(rmpt(), 'rb') as fr:
            reminder = pickle.load(fr)
            if reminder is None:
                reminder = []
    except:
        reminder = []
    return reminder

def saveReminder(data: list):
    with open(rmpt(), 'wb') as fw:
        pickle.dump(data, fw)
        fw.close()

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
    except:
        printData("Unable to load configuration file...")

while True:
    try:
        rm = loadReminder()
        if len(rm) > 0 and not rm is None:
            for reminder in rm:
                hr, mn = int(datetime.datetime.now().time().hour), int(datetime.datetime.now().time().minute)
                if hr == int(str(reminder[1]).split(":")[0]) and mn == int(str(reminder[1]).split(":")[1]):
                    speak(f"Its time for your task you told me to remind. Your task is {reminder[0]}")
                    rm = rm.remove(reminder)
                    saveReminder(rm)
        time.sleep(60)
    except Exception as ee:
        time.sleep(10)
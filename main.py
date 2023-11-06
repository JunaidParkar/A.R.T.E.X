import eel
import json
import pyttsx3

eel.init("./Fun/Body/Comp")

@eel.expose
def getSetting():
    with open('setting.json', 'r') as f:
        sd =  json.load(f)
        print(sd)
        return sd
    
@eel.expose
def updateSetting(setting, value):
    with open('setting.json', 'r') as f:
        data = json.load(f)
    data[setting] = value
    with open('setting.json', 'w') as f:
        json.dump(data, f)

@eel.expose
def get_available_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    voice_info = []
    for index, voice in enumerate(voices):
        voice_info.append({
            'index': index,
            'name': voice.name,
        })
    return voice_info

eel.start("desktop.html")
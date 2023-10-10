import eel
import json

eel.init("./Evo/Body/Comp")

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

eel.start("desktop.html")
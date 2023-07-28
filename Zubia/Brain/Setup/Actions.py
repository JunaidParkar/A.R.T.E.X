import json
import shutil
import Zubia.Brain.Paths as fp
from Zubia.Brain.Community import writeSetupLog

def updateCongif(key: str, value: str):
    with open(fp.SOFTWARE_CONFIG_FILE, "r+") as f:
        data = json.load(f)
        data[key] = value
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def storeSettings():
    writeSetupLog("Store Settings")
    shutil.copyfile(fp.SOFTWARE_CONFIG_FILE, fp.LOCALDATA_CONFIG_FILE)
    writeSetupLog("Settings stored successfully")
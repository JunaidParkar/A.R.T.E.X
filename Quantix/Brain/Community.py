import json
import os
import requests
import datetime
import pickle
from Quantix.Brain.Paths import  TEMP_FOLDER, PRIVATE_4, LOG_FILE, LOG_FOLDER
 
def checkInternet():
    try:
        response = requests.get("https://junaidparkar-f7e41.web.app", timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

def writeDataInFile(data, filename):
    if os.path.exists(filename):
        if os.path.getsize(filename) == 0:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
        else:
            try:
                with open(filename, 'r+') as file:
                    existing_data = json.load(file)
                    existing_data.update(data)
                    file.seek(0)
                    json.dump(existing_data, file, indent=4)
            except:
                with open(filename, 'w') as file:
                    json.dump(data, file, indent=4)
    else:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)



def verifyLog(path):
    if not os.path.isdir(LOG_FOLDER):
        os.mkdir(LOG_FOLDER)
    if not os.path.isfile(path):
        with open(path, "w") as f:
            f.close()


def writeLog(text):
    verifyLog(LOG_FILE)
    with open(LOG_FILE, "ab+") as process:
        process.write(f"[{datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}] {text}\n".encode("utf-8"))
        process.close()

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
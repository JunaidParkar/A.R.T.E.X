import os
import json
import sys
import shutil
import pyttsx3
sys.path.append(os.environ.get('Zubia'))
import Setup.Paths as filePaths
from Setup.Command import writeLogFile, updateCongif

FOLDER_PATHS = [[filePaths.LOCALFOLDER, "Root"], [filePaths.DATASET_FOLDER, "Dataset"], [f"{filePaths.DATABASE_FOLDER}", "Database"], [f"{filePaths.CHAT_DATA_FOLDER}", "Chats"], [f"{filePaths.TRAINED_DATA_FOLDER}", "Train"], [f"{filePaths.LOCAL_COMMUNITY_FOLDER}", "Community"]]


def storeSettings():
    writeLogFile("Store Settings")
    shutil.copyfile(filePaths.SOFTWARE_CONFIG_FILE, filePaths.LOCALDATA_CONFIG_FILE)
    writeLogFile("Settings stored successfully")


def manageChatFile():
    if os.path.exists(filePaths.CHAT_DATA_FILE):
        pass
    else:
        with open(filePaths.CHAT_DATA_FILE, "w") as f:
            json.dump([], f)
            f.close()

def setVoice():
    writeLogFile("Setting up voice")
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    i = 0
    voiceAvail = False
    for voice in voices:
        name = "Microsoft Zira Desktop - English (United States)"
        if voice.name == name:
            voiceAvail = True
            break
        else: 
            voiceAvail = False
        i = i + 1
    if voiceAvail:
        with open(filePaths.SOFTWARE_CONFIG_FILE, "r+") as f:
                    voiceSett = json.load(f)
                    voiceSett = voiceSett["voice"]
                    voiceSett["index"] = i
                    updateCongif("voice", voiceSett)
        writeLogFile("setup voice successful")
    else:
        writeLogFile("Voice not found")

def manageLocalDir():
    for folderPath in FOLDER_PATHS:
        if os.path.isdir(folderPath[0]):
            writeLogFile(f"{folderPath[1]} folder already present")
        else:
            os.mkdir(folderPath[0])
            writeLogFile(f"{folderPath[1]} folder created")

def copyIntentsToLocalDir():
    writeLogFile("Copying training data")
    shutil.copyfile(filePaths.SOFTWARE_INTENTS_FILE, filePaths.LOCALDATA_INTENTS_FILE)
    writeLogFile("Copied training data")

def setGoogleApi():
    api = input("\nEnter your api key properly: ")
    api = api.replace(" ", "").replace("\t", "")
    with open(filePaths.SOFTWARE_CONFIG_FILE, "r+") as f:
        data = json.load(f)
        data["googleAI"] = api
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
        f.close()
    writeLogFile("API stored successfully")

def configureAll():
    manageLocalDir()
    setVoice()
    copyIntentsToLocalDir()
    setGoogleApi()
    storeSettings()
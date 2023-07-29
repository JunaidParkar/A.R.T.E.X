import os
import json
import shutil
import pyttsx3
import Zubia.Brain.Paths as fp
from Zubia.Body.Hand import printData
from Zubia.Brain.Community import writeSetupLog
from Zubia.Brain.NeuralNetwork.Train import TrainAI
from Zubia.Brain.Setup.Structure import defaultConfig

def updateCongif(key: str, value: str):
    with open(fp.SOFTWARE_CONFIG_FILE, "r+") as f:
        data = json.load(f)
        data[key] = value
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def copyFile(file: str, dest: str):
    writeSetupLog(f"Copying {file} at {dest}")
    try:
        shutil.copyfile(file, dest)
        writeSetupLog(f"Copied {file} successfully at {dest}")
    except:
        writeSetupLog(f"Failed to copy {file} File at {dest}")
    
def setVoice(ind: int):
    name = "Microsoft Zira Desktop - English (United States)"
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    if voices[ind].name == name:
        pass
    else:
        writeSetupLog("Setting up voice index")
        i = 0
        voiceAvail = False

        for voice in voices:
            if voice.name == name:
                voiceAvail = True
                break
            else: 
                voiceAvail = False
            i = i + 1

        if voiceAvail:
            writeSetupLog("Setup voice index successful")
            return i
        else:
            writeSetupLog("Voice not found")
            printData("Zira voice not found on your Windows. Kindly go through the installation guide or visit the forum page at xyz to activate Zira voice on your Windows.")
            return 0

def verifyConfig():
    if not os.path.exists(fp.SOFTWARE_CONFIG_FILE):
        writeSetupLog(f"Creating config file at {fp.SOFTWARE_CONFIG_FILE}")
        with open(fp.SOFTWARE_CONFIG_FILE, 'w') as configF:
                json.dump(defaultConfig(), configF)
                configF.close()
        writeSetupLog(f"Created config file successfully at {fp.SOFTWARE_CONFIG_FILE}")
    writeSetupLog("Checking config file for any remaining settings")
    with open(fp.SOFTWARE_CONFIG_FILE, "r+") as f:
        config_data = json.load(f)
        index = setVoice(config_data["voice"]["index"])
        config_data["voice"]["index"] = index
        if config_data['googleAI'] == '':
            writeSetupLog("Storing googleAI api")
            printData("Enter your GoogleAI api key. If you dont set it then you can't use full features like chatting or any research. If you dont know how to get it then kindly visit forum at xyz. To skip this step enter '0'")
            api = input("Enter your GoogleAI api key.\t")
            if (api == 0) or (api == "0"):
                config_data['googleAI'] = ""
            else:
                config_data['googleAI'] = str(api)
            f.seek(0)
            json.dump(config_data, f, indent=4)
            f.truncate()
            f.close()
            writeSetupLog("Storing googleAI api successful")
    writeSetupLog("Checked config file for any remaining settings successful")


def verifyFolderExistance(folder_path: str):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        if (folder_path != fp.LOCALFOLDER) and (folder_path != fp.LOG_FOLDER):
            writeSetupLog(f"Created folder {folder_path}")

def verifyFileExistance(file_path: str):
    if not os.path.exists(file_path):
        if file_path == fp.LOCALDATA_CONFIG_FILE:
            verifyConfig()
            copyFile(fp.SOFTWARE_CONFIG_FILE, fp.LOCALDATA_CONFIG_FILE)
        elif file_path == fp.LOCALDATA_INTENTS_FILE:
            copyFile(fp.SOFTWARE_INTENTS_FILE, fp.LOCALDATA_INTENTS_FILE)
        elif file_path == fp.TRAINED_DATA_FILE:
            TrainAI()
        elif file_path == fp.CHAT_DATA_FILE:
            writeSetupLog("Creating chatting file")
            with open(fp.CHAT_DATA_FILE, "w") as f:
                json.dump([], f)
                f.close()
            writeSetupLog("Created chatting file successfully")
        elif file_path == fp.LOG_SETUP:
            with open(file_path, 'w') as file:
                file.close()
        else:
            writeSetupLog(f"Creating {file_path}")
            with open(file_path, 'w') as file:
                file.close()
            writeSetupLog(f"Created {file_path} successfully")
    elif file_path == fp.LOCALDATA_CONFIG_FILE:
        verifyConfig()
        copyFile(fp.SOFTWARE_CONFIG_FILE, fp.LOCALDATA_CONFIG_FILE)

def setupManager():
    verifyFolderExistance(fp.LOCALFOLDER)
    verifyFolderExistance(fp.LOG_FOLDER)
    verifyFileExistance(fp.LOG_SETUP)
    verifyFolderExistance(fp.LOCAL_COMMUNITY_FOLDER)
    verifyFileExistance(fp.LOCALDATA_CONFIG_FILE)
    verifyFolderExistance(fp.DATASET_FOLDER)
    verifyFileExistance(fp.LOCALDATA_INTENTS_FILE)
    verifyFolderExistance(fp.DATABASE_FOLDER)
    verifyFolderExistance(fp.CHAT_DATA_FOLDER)
    verifyFileExistance(fp.CHAT_DATA_FILE)
    verifyFolderExistance(fp.TRAINED_DATA_FOLDER)
    verifyFileExistance(fp.TRAINED_DATA_FILE)
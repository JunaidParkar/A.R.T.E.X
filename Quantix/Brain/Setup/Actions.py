import os
import json
import shutil
import pyttsx3
import winreg
import Quantix.Brain.Paths as fp
from Quantix.Body.Hand import printData, takeInput
from Quantix.Brain.Community import writeLog
from Quantix.Brain.Setup.Structure import defaultConfig, defaultIntents

def updateCongif(key: str, value: str):
    with open(fp.SOFTWARE_CONFIG_FILE, "r+") as f:
        data = json.load(f)
        data[key] = value
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def moveFile(filepath: str, dest: str):
    writeLog(f"moving {filepath} to {dest}")
    shutil.move(filepath, dest)
    writeLog(f"moved {filepath} to {dest}")

def copyFile(file: str, dest: str):
    writeLog(f"Copying {file} at {dest}")
    try:
        shutil.copyfile(file, dest)
        writeLog(f"Copied {file} successfully at {dest}")
    except:
        writeLog(f"Failed to copy {file} File at {dest}")
    
def setVoice(ind: int):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    writeLog("Setting up voice index")
    if ind > len(voices) or ind < 0:
        return 0
    return ind


def verifyConfig():
    if not os.path.exists(fp.SOFTWARE_CONFIG_FILE):
        writeLog(f"Creating config file at {fp.SOFTWARE_CONFIG_FILE}")
        with open(fp.SOFTWARE_CONFIG_FILE, 'w') as configF:
                json.dump(defaultConfig(), configF)
                configF.close()
        writeLog(f"Created config file successfully at {fp.SOFTWARE_CONFIG_FILE}")
    writeLog("Checking config file for any remaining settings")
    with open(fp.SOFTWARE_CONFIG_FILE, "r+") as f:
        config_data = json.load(f)
        try:
            config_data["voice"]["index"] = setVoice(config_data["voice"]["index"])
        except:
            config_data["voice"]["index"] = 0
        try:
            config_data["googleAI"] = config_data["googleAI"]
        except:
            config_data["googleAI"] = ''
        if config_data['googleAI'] == '':
            writeLog("Storing googleAI api")
            printData("Enter your GoogleAI api key. If you dont set it then you can't use full features like chatting or any research. If you dont know how to get it then kindly visit forum at xyz. To skip this step enter '0'")
            api = takeInput("Enter your GoogleAI api key.")
            if (api == 0) or (api == "0"):
                config_data['googleAI'] = ""
            else:
                config_data['googleAI'] = str(api)
            f.seek(0)
            json.dump(config_data, f, indent=4)
            f.truncate()
            f.close()
            writeLog("Storing googleAI api successful")
    writeLog("Checked config file for any remaining settings successful")
    copyFile(fp.SOFTWARE_CONFIG_FILE, fp.LOCALDATA_CONFIG_FILE)

def verifyIntents():
    if not os.path.isfile(fp.LOCALDATA_INTENTS_FILE):
        if not os.path.isfile(fp.SOFTWARE_INTENTS_FILE):
            with open(fp.SOFTWARE_INTENTS_FILE, 'w') as ff:
                ff.close()
        with open(fp.SOFTWARE_INTENTS_FILE, 'r+') as fff:
            json.dump(defaultIntents(), fff, indent=4)
            fff.close()
        copyFile(fp.SOFTWARE_INTENTS_FILE, fp.LOCALDATA_INTENTS_FILE)

def getInstalledApps():
    writeLog("Fetching installed apps")
    installed_apps = []
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall") as key:
            try:
                index = 0
                while True:
                    subkey_name = winreg.EnumKey(key, index)
                    with winreg.OpenKey(key, subkey_name) as subkey:
                        try:
                            app_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                            install_location = winreg.QueryValueEx(subkey, "InstallLocation")[0]
                            if install_location and not app_name.lower().endswith('.exe'):
                                installed_apps.append(app_name)
                        except FileNotFoundError:
                            writeLog("An unknown error occured")
                        except Exception as e:
                            writeLog(f"Error reading registry key: {e}")
                    index += 1
            except OSError:
                writeLog("Error while finding the registered apps")
    except:
        writeLog("Unable to use windows registry")
    if len(installed_apps) > 0:
        with open(fp.APPS_FILE, 'w') as json_file:
            json.dump(installed_apps, json_file, indent=4)
            writeLog("Fetched installed apps successfully")
    else:
        writeLog("No installed apps fetched")

def basicSetup():
    logPth = [fp.LOG_FILE]
    if not os.path.isdir(fp.LOCALFOLDER):
        os.mkdir(fp.LOCALFOLDER)
    if not os.path.isdir(fp.LOG_FOLDER):
        os.mkdir(fp.LOG_FOLDER)
    for log in logPth:
        if not os.path.isfile(log):
            with open(log, 'w') as f:
                f.close()

def handleStructure(paths: list):
    for folder in paths:
        if not os.path.isdir(folder):
            writeLog(f"Creating folder {folder}")
            os.mkdir(folder)

def dirSetup():
    dirs = [
        fp.LOCALFOLDER,
        fp.LOCAL_COMMUNITY_FOLDER,
        fp.DATASET_FOLDER,
        fp.DATABASE_FOLDER,
        fp.CHAT_DATA_FOLDER,
        fp.TRAINED_DATA_FOLDER,
        fp.APPS_FOLDER
    ]
    handleStructure(dirs)

# def filesSetup():

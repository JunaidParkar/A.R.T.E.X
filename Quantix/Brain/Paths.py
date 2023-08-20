import os

QUANTIX = os.environ.get('Quantix')
TEMP_FOLDER = f"{QUANTIX}\\Quantix\\Temp"

LOCALAPPDATA = os.environ['LOCALAPPDATA']
LOCALFOLDER = f"{LOCALAPPDATA}\\Quantix"

DATABASE_FOLDER = f"{LOCALFOLDER}\\Database"

CHAT_DATA_FOLDER = f"{DATABASE_FOLDER}\\Chats"
CHAT_DATA_FILE = f"{CHAT_DATA_FOLDER}\\Chats.json"

TRAINED_DATA_FOLDER = f"{DATABASE_FOLDER}\\Train"
TRAINED_DATA_FILE = f"{TRAINED_DATA_FOLDER}\\TrainedData.pth"

APPS_FOLDER = f"{DATABASE_FOLDER}\\Apps"
APPS_FILE = f"{APPS_FOLDER}\\AppsList.json"
APPS_USER_FILE = f"{APPS_FOLDER}\\UserApps.json"

LOCAL_COMMUNITY_FOLDER = f"{LOCALFOLDER}\\Community"
LOCALDATA_CONFIG_FILE = f"{LOCAL_COMMUNITY_FOLDER}\\Config.json"
SOFTWARE_CONFIG_FILE = f"{os.environ['Quantix']}\\Quantix\\Data\\Config.json"

DATASET_FOLDER = f"{LOCALFOLDER}\\Dataset"
LOCALDATA_INTENTS_FILE = f"{DATASET_FOLDER}\\Intents.json"
SOFTWARE_INTENTS_FILE = f"{os.environ['Quantix']}\\Quantix\\Brain\\Datasets\\Intents.json"

CHROME_DRIVER_FOLDER = f"{LOCALFOLDER}\\Chrome"
CHROME_DRIVER_FILE = f"{CHROME_DRIVER_FOLDER}\\Driver.exe"

LOG_FOLDER = f"{QUANTIX}\\Logs"
LOG_FILE = f"{LOG_FOLDER}\\log.txt"

REMINDER_FILE = f"{QUANTIX}\\Quantix\\Brain\\Memory\\Reminder.py"

PRIVATE_1 = "Auth.pkl"
PRIVATE_2 = "Ques.pkl"
PRIVATE_3 = "Ans.pkl"
PRIVATE_4 = "Reminder.pkl"
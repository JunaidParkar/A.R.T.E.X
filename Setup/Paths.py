import os

LOCALAPPDATA = os.environ['LOCALAPPDATA']
LOCALFOLDER = f"{LOCALAPPDATA}\\Zubia"


LOG = f"{LOCALFOLDER}\\log.txt"

DATABASE_FOLDER = f"{LOCALFOLDER}\\Database"

CHAT_DATA_FOLDER = f"{DATABASE_FOLDER}\\Chats"
CHAT_DATA_FILE = f"{DATABASE_FOLDER}\\Chats\\Chats.json"

TRAINED_DATA_FOLDER = f"{DATABASE_FOLDER}\\Train"
TRAINED_DATA_FILE = f"{TRAINED_DATA_FOLDER}\\Train\\trainedData.pth"

LOCAL_COMMUNITY_FOLDER = f"{LOCALFOLDER}\\Community"
LOCALDATA_CONFIG_FILE = f"{LOCAL_COMMUNITY_FOLDER}\\Config.json"
SOFTWARE_CONFIG_FILE = f"{os.environ['Zubia']}\\Setup\\Community\\Config.json"

DATASET_FOLDER = f"{LOCALFOLDER}\\Dataset"
LOCALDATA_INTENTS_FILE = f"{DATASET_FOLDER}\\Intents.json"
SOFTWARE_INTENTS_FILE = f"{os.environ['Zubia']}\\Setup\\Community\\Intents.json"
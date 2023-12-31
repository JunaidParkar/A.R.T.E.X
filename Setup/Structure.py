import os
import Management.Paths.DataPath as fp
from Fun.Brain.Community import writeLog

FOLDER_PATHS = [[fp.LOCALFOLDER, "Root"], [fp.DATASET_FOLDER, "Dataset"], [f"{fp.DATABASE_FOLDER}", "Database"], [f"{fp.CHAT_DATA_FOLDER}", "Chats"], [f"{fp.TRAINED_DATA_FOLDER}", "Train"], [f"{fp.LOCAL_COMMUNITY_FOLDER}", "Community"], ["Logs", "Logs"]]

def defaultConfig():
    return {"voice": {"index": 0,"rate": 135 }, "microphone": {"pause_treshold": 1, "min_listen_timer": 0, "max__listen_timer": 8 }, "googleAI": ""}

def defaultIntents():
    return { "intents": [{"tag": "open", "patterns": ["open", "launch", "start", "visit"], "responses": ["open"]},{"tag": "whatsapp", "patterns": ["whatsapp", "message"], "responses": ["whatsapp"]},{ "tag": "exit", "patterns": ["exit"], "responses": ["exit"]},{ "tag": "sleep", "patterns": ["sleep"], "responses": ["sleep"]},{ "tag": "reminder", "patterns": ["remind", "reminder"], "responses": ["reminder"]}]}



def manageLocalDir():
    for folderPath in FOLDER_PATHS:
        if os.path.isdir(folderPath[0]):
            writeLog(f"{folderPath[1]} folder already present")
        else:
            os.mkdir(folderPath[0])
            writeLog(f"{folderPath[1]} folder created")
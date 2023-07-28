import os
import json
import shutil
import pyttsx3
import Zubia.Brain.Paths as fp
from Zubia.Brain.Community import writeSetupLog

FOLDER_PATHS = [[fp.LOCALFOLDER, "Root"], [fp.DATASET_FOLDER, "Dataset"], [f"{fp.DATABASE_FOLDER}", "Database"], [f"{fp.CHAT_DATA_FOLDER}", "Chats"], [f"{fp.TRAINED_DATA_FOLDER}", "Train"], [f"{fp.LOCAL_COMMUNITY_FOLDER}", "Community"], ["Logs", "Logs"]]



def manageLocalDir():
    for folderPath in FOLDER_PATHS:
        if os.path.isdir(folderPath[0]):
            writeSetupLog(f"{folderPath[1]} folder already present")
        else:
            os.mkdir(folderPath[0])
            writeSetupLog(f"{folderPath[1]} folder created")
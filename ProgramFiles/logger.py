import os
from datetime import datetime

class Logger():

    def __init__(self, fileName: str):
        self.fileName = fileName
        self.path = os.getcwd()

    def getDate(self):
        now = datetime.now()
        return now.strftime("%H:%M:%S %Y-%m-%d")

    def writeLog(self, msg: str):
        with open(os.path.join(self.path, f"{self.fileName}.txt"), 'a') as file:
            file.write(f"{self.getDate()} {msg}\n")
            file.close()
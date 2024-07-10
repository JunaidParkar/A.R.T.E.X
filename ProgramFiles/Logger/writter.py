import os
from datetime import datetime

class LogWritter():

    def __init__(self, fileName: str):
        self.__fileName = fileName
        self.__path = os.getcwd()

    def __getDate(self):
        now = datetime.now()
        return now.strftime("%H:%M:%S %Y-%m-%d")

    def writeLog(self, msg: str):
        with open(os.path.join(self.__path, f"{self.__fileName}.txt"), 'a') as file:
            file.write(f"{self.__getDate()} {msg}\n")
            file.close()
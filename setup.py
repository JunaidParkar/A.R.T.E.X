import os
import shutil
import json
import sys
sys.path.append(os.environ.get('Zubia'))
from datetime import datetime
import Setup.Paths as filePaths
from Setup.Organizer import setVoice, copyIntentsToLocalDir, setGoogleApi, manageChatFile, manageLocalDir, storeSettings, configureAll

manageLocalDir()
manageChatFile()


options = [["Set voices", 1], ["Load training data", 2], ["Set google api", 3], ["Store settings", 4], ["Configure all", 5], ["Exit", 99]]

def process_choice(choice):
    if choice == 1:
        setVoice()
    elif choice == 2:
        copyIntentsToLocalDir()
    elif choice == 3:
        setGoogleApi()
    elif choice == 4:
        storeSettings()
    elif choice == 5:
        configureAll()

while True:
    print("\nEnter option numbers only...\n")
    for option in options:
        print(f"{option[1]} {option[0]}")
    choice = int(input("\nEnter the option number: "))
    if choice == 99:
        break
    else:
        process_choice(choice)
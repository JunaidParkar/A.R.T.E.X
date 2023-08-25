import os
os.system("cls" if os.name == "nt" else "clear")
os.system('title Evo AI 1.0.1')
import subprocess
import time

def setEnv():
    os.environ["Evo"] = os.getcwd()
    try:
        subprocess.run(['setx', "Evo", os.getcwd()], check=True)
        print("Evo: Your PC will restart in 1 minute. Please save all your pending work. Or you can close me and complete your work and restart your PC manually...")
        time.sleep(60)
        os.system("shutdown /r /t 1")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while setting the environment variable: {e}")

if os.environ.get("Evo") is None:
    setEnv()
if not os.environ.get("Evo") == os.getcwd():
    setEnv()

# setup starts

from Evo.Brain.Setup.Actions import dirSetup, verifyConfig, verifyIntents, getInstalledApps

dirSetup()
verifyConfig()
verifyIntents()
getInstalledApps()

from Evo.Body.Mouth import speak
from Evo.Brain.NeuralNetwork.Train import TrainAI

TrainAI()

# from Evo.Brain.Community import checkInternet
# checkInternet()

# from Evo.Brain.Setup.Chrome import checkChromeSetUp, driverSetup, removeSeleniumBackups

# removeSeleniumBackups()
# # setupManager()
# isChrome = checkChromeSetUp()
# if isChrome is True:
#     driverSetup()
# else:
#     speak(isChrome)
#     sys.exit()

# authenticate

import sys
from Evo.Brain.Security.Authentication import Authenticate
auth = Authenticate()
if auth is True:
    speak("You are logged in")
else:
    speak(f"Exiting: {auth}")
    time.sleep(1)
    sys.exit()

from Evo.Brain.Paths import REMINDER_FILE

subprocess.Popen(["python", REMINDER_FILE])
speak("Please do not close the reminder window as it is a part of me...")

# main AI starts

from Evo.Body.Ear import listen
from Evo.Body.Mouth import speak
from Evo.Brain.Palm.Chat import chatBot
from Evo.Brain.Memory.Remind import addReminder
from Evo.Brain.Features.AppOpener import openApp
from Evo.Brain.NeuralNetwork.Model import TasksExecutor


while True:
    query = listen()
    if len(query) > 3:
        task = TasksExecutor(query)
        if not task is None:
            task = TasksExecutor(query)
            if "open" in task:
                openApp(query)
            elif "exit" in task:
                speak("Exiting please wait")
                break
            elif "sleep" in task:
                speak("Sleeping mode started. Wake me up by calling me...")
            elif "reminder" in task:
                addReminder()
        else:
            resp = chatBot(query)
            speak(resp)
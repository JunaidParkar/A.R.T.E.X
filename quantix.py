import os
os.system("cls" if os.name == "nt" else "clear")
os.system('title Quantix AI 1.0.1')
import subprocess
import time
if os.environ.get("Quantix") is None:
    os.environ["Quantix"] = os.getcwd()
    try:
        subprocess.run(['setx', "Quantix", os.getcwd()], check=True)
        print("Quantix: Your PC will restart in 1 minute. Please save all your pending work. Or you can close me and complete your work and restart your PC manually...")
        time.sleep(60)
        os.system("shutdown /r /t 1")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while setting the environment variable: {e}")

# setup starts

# from Quantix.Brain.Setup.Actions import setupManager
from Quantix.Body.Mouth import speak

# authenticate

import sys
import time
from Quantix.Brain.Security.Authentication import Authenticate
auth = Authenticate()
if auth is True:
    speak("You are logged in")
else:
    speak(f"Exiting: {auth}")
    time.sleep(1)
    sys.exit()

from Quantix.Brain.Setup.Chrome import checkChromeSetUp, driverSetup, removeSeleniumBackups

removeSeleniumBackups()
# setupManager()
isChrome = checkChromeSetUp()
if isChrome is True:
    driverSetup()
else:
    speak(isChrome)
    sys.exit()

# main AI starts

import Quantix.Brain.Paths as fp
from Quantix.Body.Ear import listen
from Quantix.Body.Mouth import speak
import Quantix.Brain.NeuralNetwork.Train
from Quantix.Brain.Palm.Chat import chatBot
from Quantix.Brain.Features.AppOpener import openApp
from Quantix.Brain.Community import checkInternet
from Quantix.Brain.NeuralNetwork.Model import TasksExecutor

while True:

    # query = input("type: ")
    query = listen()
    # isInter = checkInternet()
    # if isInter:
    if len(query) > 3:
    
        if "open" in query or "message" in query or "start" in query or "visit" in query or "launch" in query or "exit" in query or "sleep mode" in query:
            task = TasksExecutor(query)
            if "open" in task:
                openApp(query)
            elif "exit" in task:
                speak("Exiting please wait")
                break
            elif "sleep" in task:
                speak("Sleeping mode started. Wake me up by calling me...")
        else:
            resp = chatBot(query)
            speak(resp)
    # else:
    #     speak("Please turn on the internet")

    # if len(query) < 3:
    #     pass
    # elif "exit" in query:
    #     break
    # else:
    #     resp = chatBot(query)
    #     speak(resp)
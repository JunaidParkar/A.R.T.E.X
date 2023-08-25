import os
import keyboard
import pyautogui
import string
from time import sleep
import os
import sys
sys.path.append(os.environ.get('Evo'))
from Evo.Body.Mouth import speak
from Evo.Brain.NeuralNetwork.Model import appFinder

def openApp(query: str):
    query = str(query).lower()

    removableQuery = ["visit", "website", "open", "start", "launch"]

    
    if "open" in query or "launch" in query or "start" in query:
        try:
            inValid = False
            for char in query:
                if char not in string.ascii_letters and char != " ":
                    print(char)
                    inValid = True
            if inValid:
                speak("Enter query properly by valid...")
            else:
                app_name = appFinder(str(query))
                if app_name is False:
                    speak("App you asked is not installed...")
                else:
                    speak(f"opening {app_name}")
                    pyautogui.press('win')
                    sleep(3)
                    keyboard.write(app_name)
                    sleep(3)
                    keyboard.press('enter')
        except:
            speak("Enter query properly by except...")
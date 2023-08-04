import os
import keyboard
import pyautogui
import string
import webbrowser
from time import sleep
import os
import sys
sys.path.append(os.environ.get('Zubia'))
from Zubia.Body.Mouth import speak
from Zubia.Brain.NeuralNetwork.Model import appFinder

def launcher(query: str):
    query = str(query).lower()

    removableQuery = ["visit", "website", "open", "start", "launch"]

    if "visit" in query:
        for wd in removableQuery:
            query = query.replace(wd, "")
        if "." in query:
            pass
        else:
            query = f"{query}.com"
        speak(f"Visiting {query}")
        link = f"http://www.{query}".replace(" ", "")
        webbrowser.open(link)
        return True
    elif "open" in query or "launch" in query or "start" in query:
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
                    speak("Your app is not installed...")
                else:
                    speak(f"opening {app_name}")
                    pyautogui.press('win')
                    sleep(1)
                    keyboard.write(app_name)
                    sleep(1)
                    keyboard.press('enter')
        except:
            speak("Enter query properly by except...")
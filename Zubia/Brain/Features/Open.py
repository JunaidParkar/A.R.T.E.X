import os
import keyboard
import pyautogui
import webbrowser
from time import sleep
import os
import sys
sys.path.append(os.environ.get('Zubia'))
from Zubia.Body.Mouth import speak

def openExe(query: str):
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
        for wod in removableQuery:
            query = query.replace(wod, "")
        speak(f"Opening {query}")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(query)
        sleep(1)
        keyboard.press('enter')
        return True
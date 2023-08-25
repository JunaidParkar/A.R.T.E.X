import os
import sys
sys.path.append(os.environ.get('Evo'))
import time
import datetime
from Evo.Body.Mouth import speak
from Evo.Brain.Community import loadReminder, saveReminder

while True:
    rm = loadReminder()
    if len(rm) > 0 and not rm is None:
        for reminder in rm:
            hr, mn = int(datetime.datetime.now().time().hour), int(datetime.datetime.now().time().minute)
            if hr == int(str(reminder[1]).split(":")[0]) and mn == int(str(reminder[1]).split(":")[1]):
                speak(f"Its time for your task you told me to remind. Your task is {reminder[0]}")
                rm = rm.remove(reminder)
                saveReminder(rm)
    time.sleep(60)
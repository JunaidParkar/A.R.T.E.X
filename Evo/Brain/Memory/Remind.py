import os
import sys
sys.path.append(os.environ.get('EvoAI'))
import re
import datetime
from Evo.Body.Ear import listen
from Evo.Body.Mouth import speak
from Evo.Brain.NeuralNetwork.Base import tokenize
from Evo.Brain.Community import saveReminder, loadReminder

def verify_time_format(time_str: str):
    pattern = r'^(\d+) (hour|hours|minute|minutes) (\d+) (hour|hours|minute|minutes)$'
    match = re.match(pattern, time_str)
    if match is None:
        return False
    return True

def addReminder():
    while True:
        speak("What task you want to be remind of:")
        task = str(listen())
        if "exit" in tokenize(task):
            return
        if len(task) > 3:
            while True:
                speak("Say the time to get you reminded. (Example, 16 hour 30 minute):")
                tm1 = str(listen()).lower()
                if 'and' in tokenize(tm1):
                    tm1 = " ".join([item for item in tokenize(tm1) if not item == 'and'])
                ver = verify_time_format(tm1)
                if ver is True:
                    tm2 = tokenize(tm1)
                    minInd = 0
                    hrInd = 0
                    if "minute" in tm2:
                        minInd = tm2.index("minute")
                    if "minutes" in tm2:
                        minInd = tm2.index("minutes")
                    if "hour" in tm2:
                        hrInd = tm2.index("hour")
                    if "hours" in tm2:
                        hrInd = tm2.index("hours")
                    hr, mn = int(tm2[hrInd - 1]), int(tm2[minInd - 1])
                    if hr <= 23 and hr >= 0 and mn <= 59 and mn >= 0:
                        break
                    speak("Please say proper time...")
                else:
                    speak("Please follow the time format...")
            remindTime = datetime.time(hour=hr, minute=mn)
            daily = False
            while True:
                speak("Do you want me to remind it daily? (yes or no):")
                rep = str(listen()).lower()
                if rep == "yes":
                    daily = True
                    break
                elif rep == "no":
                    daily = False
                    break
                else:
                    speak("Sorry i did not understand what you said...")
            speak("Please verify the reminder...")
            speak(f"You asked me to remind to {task} at {remindTime} {'daily' if daily else ''}")
            while True:
                speak("Do you want to save this reminder? (yes or no)")
                save = str(listen()).lower()
                if save == "yes":
                    finalisedReminder = [task, remindTime, daily]
                    speak("Saving reminder")
                    lr = loadReminder()
                    lr.append(finalisedReminder)
                    saveReminder(lr)
                    speak("Your reminder is set")
                    return
                elif save == "no":
                    break
                else:
                    speak("Sorry sir! I could not understand what you just said...")
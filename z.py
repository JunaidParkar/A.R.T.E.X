from Quantix.Body.Hand import takeInput
from Quantix.Body.Ear import listen
from Quantix.Body.Mouth import speak
from Quantix.Brain.NeuralNetwork.Base import tokenize
import datetime
import re

def verify_time_format(time_str):
    pattern = r'^(\d+) (hour|hours|minute|minutes) and (\d+) (hour|hours|minute|minutes)$'
    match = re.match(pattern, time_str)
    if match:
        return False
    return True

def addReminder():
    while True:
        task = takeInput("What task you want to be remind of:")
        if "exit" in tokenize(task) or "reminder" in tokenize(task):
            return
        while True:
            tm1 = str(takeInput("Say the time to get you reminded. (Example, 16 hour 30 minute):")).lower()
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
                print(hr, mn)
                if hr <= 24 and hr >= 0 and mn <= 60 and mn >= 0:
                    break
                speak("Please say proper time...")
            else:
                speak("Please follow the time format...")
        remindTime = datetime.time(hour=hr, minute=mn)
        while True:
            rep = takeInput("Do you want me to remind it daily? (yes or no):").lower()
            if rep == "yes":
                break
            elif rep == "no":
                speak("ok sir! What else can i help you with?")
                return
            else:
                speak("Sorry i did not understand what you said...")
        speak("Please verify the reminder...")
        speak(f"You asked me to remind to {task} at {remindTime} {'daily' if rep == 'yes' else ''}")
        speak("Do you want to save this reminder? (yes or no)")
        save = takeInput(">>")
        if save == "yes":
            print("saving reminder")
        elif save == "no":
            pass
        else:
            speak("Sorry sir! I could not understand what you just said...")

addReminder()

# a = ["hy"]
# a.index(a)
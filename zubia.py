import os
import sys
import subprocess
if os.environ['Zubia'] is None:
    os.environ["Zubia"] = os.getcwd()
    try:
        subprocess.run(['setx', "Zubia", os.getcwd()], check=True)
        sys.exit()
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while setting the environment variable: {e}")
import Zubia.Brain.Paths as fp
from Zubia.Body.Ear import listen
from Zubia.Body.Mouth import speak
import Zubia.Brain.NeuralNetwork.Train
from Zubia.Brain.Palm.Chat import chatBot
from Zubia.Brain.Features.Open import openExe
from Zubia.Brain.Community import checkInternet
from Zubia.Brain.NeuralNetwork.Model import TasksExecutor

while True:

    query = input("type: ")
    isInter = checkInternet()
    if isInter:

    
        if "open" in query or "message" in query or "start" in query or "visit" in query or "launch" in query or "exit" in query or "sleep mode" in query:
            task = TasksExecutor(query)
            if "open" in task:
                openExe(query)
            elif "exit" in task:
                speak("Exiting please wait")
                break
            elif "sleep" in task:
                speak("Sleeping mode started. Wake me up by calling me...")
        else:
            resp = chatBot(query)
            speak(resp)
    else:
        speak("Please turn on the internet")

    # if len(query) < 3:
    #     pass
    # elif "exit" in query:
    #     break
    # else:
    #     resp = chatBot(query)
    #     speak(resp)
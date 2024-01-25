import os
os.system('title Artex AI 3.0.0')
import subprocess
import time

def setEnv():
    os.environ["ARTEX"] = os.getcwd()
    try:
        subprocess.run(['setx', "ARTEX", os.getcwd()], check=True)
        print("Artex: Your PC will restart in 1 minute. Please save all your pending work. Or you can close me and complete your work and restart your PC manually...")
        time.sleep(60)
        os.system("shutdown /r /t 1")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while setting the environment variable: {e}")

if os.environ.get("ARTEX") is None:
    setEnv()
if not os.environ.get("ARTEX") == os.getcwd():
    setEnv()
from NeuralNetwork.Model import TasksExecutor

folders = ["Systems", "Systems/Datasets"]

def create_folders(folder_names):
    for folder_name in folder_names:
        try:
            os.makedirs(folder_name)
            print(f"Folder '{folder_name}' created successfully.")
        except FileExistsError:
            print(f"Folder '{folder_name}' already exists.")

# create_folders(folders)

# import Admin.train
from Functions.Base import speak

import shutil
from Variables.Envirenments import DATASET_FILE, TRAINED_DATASET_FILE
from NeuralNetwork.Palm import chatBot
import re
import markdown
from markdown.extensions.fenced_code import FencedCodeExtension
from bs4 import BeautifulSoup

def move_specific_file(destination_folder, file_name):
    try:
        os.makedirs(destination_folder, exist_ok=True)
        shutil.move(file_name, destination_folder)
        print(f"File '{file_name}' moved successfully to '{destination_folder}'.")
    except Exception as e:
        print(f"Error: {e}")


destination_directory = "Systems/Datasets"
specific_file_name = "Intents.bin"
specific_file_name1 = "Trained_intents.pth"

move_specific_file(destination_directory, specific_file_name)


move_specific_file(destination_directory, specific_file_name1)
        
def remove_markdown(text):
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    text = re.sub(r'\*', '', text)
    return text

while True:
    inp = input(">> ")
    if inp == "exit":
        break
    else:
        ans = TasksExecutor(inp)
        if not ans:
            ans = chatBot(inp)
            try:
                ans = markdown.markdown(ans, extensions=[FencedCodeExtension()])
            except:
                ans = "I am sorry, I am unable to answer your query as i am still learning stuffs."
        html = markdown.markdown(ans)
        soup = BeautifulSoup(html, features='html.parser')
        speak(soup.get_text().replace("|", "").replace("-", "").replace("#", "").replace("*", ""))
import os
import sys
sys.path.append(os.environ.get('ARTEX'))
from NeuralNetwork.Model import TasksExecutor
from Trainer.Train import TrainAI

folders = ["Systems", "Systems/Datasets"]

def create_folders(folder_names):
    for folder_name in folder_names:
        try:
            os.makedirs(folder_name)
            print(f"Folder '{folder_name}' created successfully.")
        except FileExistsError:
            print(f"Folder '{folder_name}' already exists.")

create_folders(folders)

import Admin.train

import shutil
from Variables.Envirenments import DATASET_FILE, TRAINED_DATASET_FILE

def move_specific_file(destination_folder, file_name):
    try:
        # Create the destination folder if it doesn't exist
        os.makedirs(destination_folder, exist_ok=True)
        shutil.move(file_name, destination_folder)
        print(f"File '{file_name}' moved successfully to '{destination_folder}'.")
    except Exception as e:
        print(f"Error: {e}")


destination_directory = "Systems/Datasets"
specific_file_name = "Intents.bin"
specific_file_name1 = "Trained_intents.pth"

move_specific_file(destination_directory, specific_file_name)

TrainAI()

# move_specific_file(destination_directory, specific_file_name)

while True:
    inp = input(">> ")
    if inp == "exit":
        break
    else:
        print(TasksExecutor(inp))
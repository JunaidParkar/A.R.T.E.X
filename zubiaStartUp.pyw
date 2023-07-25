import subprocess
import os

os.chdir(os.environ.get("Zubia"))
print(os.getcwd())

subprocess.run(["python", "./Zubia/Brain/NeuralNetwork/Train.py"])

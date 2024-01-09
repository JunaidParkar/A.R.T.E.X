import os
import sys
sys.path.append(os.environ.get('ARTEX'))
print(os.environ.get('ARTEX'))

from NeuralNetwork.Model import TasksExecutor

while True:
    inp = input(">> ")
    if inp == "exit":
        break
    else:
        print(TasksExecutor(inp))
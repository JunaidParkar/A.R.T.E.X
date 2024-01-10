import pickle
import json

import pickle

def write_binary_file(data, filename):
    serialized_data = pickle.dumps(data)

    with open(filename, 'wb') as file:
        file.write(serialized_data)

def read_binary_file(filename):
    with open(filename, 'rb') as file:
        serialized_data = file.read()
    data = pickle.loads(serialized_data)

    return data

with open("intents.json", 'r') as jd:
    intents = json.load(jd)
write_binary_file(intents, 'binary_data.bin')

# read_data = read_binary_file('binary_data.bin')
# print("Read Data:", read_data)

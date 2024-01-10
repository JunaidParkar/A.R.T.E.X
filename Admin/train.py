import os
import sys
sys.path.append(os.environ.get('ARTEX'))
from Admin.Worker.Base import write_binary_file
import json

intent_file = "Admin/intents.json"
dataset_file = "Intents.bin"

with open(intent_file, 'r') as it:
    intents = json.load(it)

write_binary_file(intents, dataset_file)
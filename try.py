import torch
import json

def opt(data):
    torch.save(data, "data.pth")

def rd():
    fd = torch.load("data.pth")
    print(fd)

def createAnswerSheet():
    with open("intents.json", 'r') as jd:
        intents = json.load(jd)

    d = {"intents": []}

    for data in intents['intents']:
        tag = data['tag']
        resp = data['responses']
        d['intents'].append({'tag': tag, 'responses': resp})
    opt(d)

# createAnswerSheet()
rd()
import torch.nn as nn
import json
import torch
import random
import os
import sys
sys.path.append(os.environ.get('Zubia'))
import Zubia.Brain.Paths as fp
from Zubia.Brain.NeuralNetwork.Base import bag_of_words, tokenize, wordsFilter, wordPercentageCalculator

def TasksExecutor(query):

    class NeuralNet(nn.Module):

        def __init__(self,input_size,hidden_size,num_classes):
            super(NeuralNet,self).__init__()
            self.l1 = nn.Linear(input_size,hidden_size)
            self.l2 = nn.Linear(hidden_size,hidden_size)
            self.l3 = nn.Linear(hidden_size,num_classes)
            self.relu = nn.ReLU()

        def forward(self,x):
            out = self.l1(x)
            out = self.relu(out)
            out = self.l2(out)
            out = self.relu(out)
            out = self.l3(out)
            return out

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    with open(fp.LOCALDATA_INTENTS_FILE,'r') as json_data:
        intents = json.load(json_data)

    FILE = fp.TRAINED_DATA_FILE
    data = torch.load(FILE)

    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data["all_words"]
    tags = data["tags"]
    model_state = data["model_state"]

    model = NeuralNet(input_size,hidden_size,output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()

    sentence = str(query)

    sentence = tokenize(sentence)
    X = bag_of_words(sentence,all_words)
    X = X.reshape(1,X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)

    _ , predicted = torch.max(output,dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output,dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:

        for intent in intents['intents']:

            if tag == intent["tag"]:

                reply = random.choice(intent["responses"])
                
                return reply
            

def appFinder(query: str):
    with open(fp.APPS_FILE, 'r') as f:
        with open(fp.APPS_USER_FILE, 'r') as uf:
            apps = json.load(f)
            userApps = json.load(uf)
            for userApp in userApps:
                apps.append(userApp)
            tokenised_apps = []
            tokenised_query = tokenize(query)
            for app in apps:
                tokenised_apps.append(tokenize(app))
            filtered_word = wordsFilter(tokenised_apps, tokenised_query)
            percentile = wordPercentageCalculator(tokenised_query, filtered_word)
            if len(percentile) == 1 and percentile[0] == -1:
                return False
            else:
                maxIndex = percentile.index(max(percentile))
                return apps[maxIndex]
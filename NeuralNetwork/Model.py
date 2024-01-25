import os
import sys
sys.path.append(os.environ.get('ARTEX'))
import json
import random
# from Management.Paths.DataPath import LOCALDATA_INTENTS_FILE, TRAINED_DATA_FILE, APPS_FILE, APPS_USER_FILE
# from Base import bag_of_words, tokenize, wordsFilter, wordPercentageCalculator
# from NeuralNetwork.Base import bag_of_words, tokenize, read_binary_file
# from Variables.Envirenments import DATASET_FILE, TRAINED_DATASET_FILE

from Variables.Envirenments import DB1, DB2
from NeuralNetwork.Base import tokenize, wordPercentageCalculator, read_binary_file

accuracy = 75

def artex(query: str):
    datasets = read_binary_file(DB1)
    responses = read_binary_file(DB2)

    query = tokenize(query)
    query = [qry.lower() for qry in query]

    filtered_responses_1 = []

    for index, dataset in enumerate(datasets):
        found_response = []
        for word in query:
            if word in dataset[1] and dataset[1] not in found_response:
                filtered_responses_1.append([index, dataset[1]])
                found_response.append(dataset[1])

    with open("text.txt", 'w+') as file:
        for item in filtered_responses_1:
            file.write(f"{item}\n")


    percentages = wordPercentageCalculator(query, filtered_responses_1)
    if percentages[0] == -1:
        return -1
    max_index, max_percentage = max(enumerate(percentages), key=lambda x: x[1])
    max_percentage = max(percentages)

    if max_percentage >= accuracy:
        indices_with_max_percentage = [index for index, percentage in enumerate(percentages) if percentage == max_percentage]
        tags_index = [filtered_responses_1[ind] for ind in indices_with_max_percentage]
        tag = []
        quest = []
        for tag_index in tags_index:
            tag.append(datasets[tag_index[0]][0])
            quest.append(datasets[tag_index[0]][1])
        tag = list(set(tag))
        if len(tag) > 1:
            resp = [' '.join(qu) + " or" if idx < len(quest) - 1 else ' '.join(qu) for idx, qu in enumerate(quest)]
            respond = [f"{' '.join(resp)}"]
            return [None, f"Do you say, {respond[0]}"]
        return [tag[0], random.choice(responses[tag[0]])]
    else:
        return [-1]

# class NeuralNet(nn.Module):
#     def __init__(self, input_size, hidden_size, num_classes):
#         super(NeuralNet, self).__init__()
#         self.l1 = nn.Linear(input_size, hidden_size)
#         self.l2 = nn.Linear(hidden_size, hidden_size)
#         self.l3 = nn.Linear(hidden_size, num_classes)
#         self.relu = nn.ReLU()

#     def forward(self, x):
#         out = self.l1(x)
#         out = self.relu(out)
#         out = self.l2(out)
#         out = self.relu(out)
#         out = self.l3(out)
#         return out

# def TasksExecutor(query):
#     device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#     intents = read_binary_file(DATASET_FILE)

#     # FILE = TRAINED_DATA_FILE
#     data = torch.load(TRAINED_DATASET_FILE)

#     input_size = data["input_size"]
#     hidden_size = data["hidden_size"]
#     output_size = data["output_size"]
#     all_words = data["all_words"]
#     tags = data["tags"]
#     model_state = data["model_state"]

#     model = NeuralNet(input_size, hidden_size, output_size).to(device)
#     model.load_state_dict(model_state)
#     model.eval()

#     sentence = str(query)

#     sentence = tokenize(sentence)
#     X = bag_of_words(sentence, all_words)
#     X = X.reshape(1, X.shape[0])
#     X = torch.from_numpy(X).to(device)

#     output = model(X)
#     _, predicted = torch.max(output / 0.01, dim=1)

#     tag = tags[predicted.item()]
#     print(f"predicted {predicted.item()}")
#     probs = torch.softmax(output / 0.8, dim=1)
#     prob = probs[0][predicted.item()]

#     print(prob.item())

#     if prob.item() > 0.95:
#         for intent in intents['intents']:
#             if tag == intent["tag"]:
#                 reply = random.choice(intent["responses"])
#                 return reply
#     return None

# def TasksExecutor(query):

#     class NeuralNet(nn.Module):

#         def __init__(self,input_size,hidden_size,num_classes):
#             super(NeuralNet,self).__init__()
#             self.l1 = nn.Linear(input_size,hidden_size)
#             self.l2 = nn.Linear(hidden_size,hidden_size)
#             self.l3 = nn.Linear(hidden_size,num_classes)
#             self.relu = nn.ReLU()

#         def forward(self,x):
#             out = self.l1(x)
#             out = self.relu(out)
#             out = self.l2(out)
#             out = self.relu(out)
#             out = self.l3(out)
#             return out

#     device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#     intents = read_binary_file(DATASET_FILE)

#     # FILE = TRAINED_DATA_FILE
#     data = torch.load(TRAINED_DATASET_FILE)

#     input_size = data["input_size"]
#     hidden_size = data["hidden_size"]
#     output_size = data["output_size"]
#     all_words = data["all_words"]
#     tags = data["tags"]
#     model_state = data["model_state"]

#     model = NeuralNet(input_size,hidden_size,output_size).to(device)
#     model.load_state_dict(model_state)
#     model.eval()

#     sentence = str(query)

#     sentence = tokenize(sentence)
#     X = bag_of_words(sentence,all_words)
#     X = X.reshape(1,X.shape[0])
#     X = torch.from_numpy(X).to(device)

#     output = model(X)
#     _ , predicted = torch.max(output/0.01,dim=1)

#     tag = tags[predicted.item()]
#     print(f"predicted {predicted.item()}")
#     probs = torch.softmax(output/0.8,dim=1)
#     prob = probs[0][predicted.item()]

#     print(prob.item())
    
#     if prob.item() > 0.95:

#         for intent in intents['intents']:
            
#             if tag == intent["tag"]:

#                 reply = random.choice(intent["responses"])
                
#                 return reply
            

# def appFinder(query: str):
#     with open(APPS_FILE, 'r') as f:
#         # with open(APPS_USER_FILE, 'r') as uf:
#             apps = json.load(f)
#             if apps is None:
#                 apps = []
#             # userApps = json.load(uf)
#             # for userApp in userApps:
#             #     apps.append(userApp)
#             tokenized_apps = []
#             tokenized_query = tokenize(query)
#             for app in apps:
#                 tokenized_apps.append(tokenize(app))
#             filtered_word = wordsFilter(tokenized_apps, tokenized_query)
#             percentile = wordPercentageCalculator(tokenized_query, filtered_word)
#             if len(percentile) == 1 and percentile[0] == -1:
#                 return False
#             else:
#                 maxIndex = percentile.index(max(percentile))
#                 return apps[maxIndex]
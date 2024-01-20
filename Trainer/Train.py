import os
import sys
sys.path.append(os.environ.get('ARTEX'))
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import torch
import numpy as np
import os
from Trainer.Base import tokenize, stem, bag_of_words, read_binary_file
from Variables.Envirenments import DATASET_FILE, TRAINED_DATASET_FILE


# def TrainAI():
#     print("Let me have some seconds to get trained\n")

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

#     intents = read_binary_file(DATASET_FILE)

#     all_words = []
#     tags = []
#     xy = []

#     for intent in intents['intents']:
#         tag = intent['tag']
#         tags.append(tag)

#         for pattern in intent['patterns']:
#             w = tokenize(pattern)
#             all_words.extend(w)
#             xy.append((w,tag))

#     ignore_words = [',','?','/','.','!']
#     all_words = [stem(w) for w in all_words if w not in ignore_words]
#     all_words = sorted(set(all_words))
#     tags = sorted(set(tags))

#     x_train = []
#     y_train = []

#     for (pattern_sentence,tag) in xy:
#         bag = bag_of_words(pattern_sentence,all_words)
#         x_train.append(bag)

#         label = tags.index(tag)
#         y_train.append(label)

#     x_train = np.array(x_train)
#     y_train = np.array(y_train)

#     num_epochs = 175
#     batch_size = 8
#     learning_rate = 0.001
#     input_size = len(x_train[0])
#     hidden_size = 5
#     output_size = len(tags)

#     class ChatDataset(Dataset):

#         def __init__(self):
#             self.n_samples = len(x_train)
#             self.x_data = x_train
#             self.y_data = y_train

#         def __getitem__(self,index):
#             return self.x_data[index],self.y_data[index]

#         def __len__(self):
#             return self.n_samples
        
#     dataset = ChatDataset()

#     train_loader = DataLoader(dataset=dataset,
#                                 batch_size=batch_size,
#                                 shuffle=True,
#                                 num_workers=0)

#     device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#     model = NeuralNet(input_size,hidden_size,output_size).to(device=device)
#     criterion = nn.CrossEntropyLoss()
#     optimizer = torch.optim.Adam(model.parameters(),lr=learning_rate)

#     for epoch in range(num_epochs):
#         for (words,labels)  in train_loader:
#             words = words.to(device)
#             labels = labels.to(dtype=torch.long).to(device)
#             outputs = model(words)
#             loss = criterion(outputs,labels)
#             optimizer.zero_grad()
#             loss.backward()
#             optimizer.step()

#         if (epoch+1) % 100 ==0:
#             print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

#     print(f'Final Loss : {loss.item():.4f}')

#     data = {
#     "model_state":model.state_dict(),
#     "input_size":input_size,
#     "hidden_size":hidden_size,
#     "output_size":output_size,
#     "all_words":all_words,
#     "tags":tags
#     }

#     torch.save(data, TRAINED_DATASET_FILE)

#     print("Training completed successfully")


class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.l2 = nn.Linear(hidden_size, hidden_size)
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        return out

class ChatDataset(Dataset):
    def __init__(self, x_data, y_data):
        self.n_samples = len(x_data)
        self.x_data = x_data
        self.y_data = y_data

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.n_samples

def train_model(model, train_loader, num_epochs, criterion, optimizer, scheduler, device):
    for epoch in range(num_epochs):
        model.train()
        for words, labels in train_loader:
            words = words.to(device)
            labels = labels.to(dtype=torch.long).to(device)
            outputs = model(words)
            loss = criterion(outputs, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        # Learning rate scheduling
        scheduler.step()

        if (epoch + 1) % 100 == 0:
            print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

    print(f'Final Loss: {loss.item():.4f}')

def TrainAI():
    print("Let me have some seconds to get trained\n")

    intents = read_binary_file(DATASET_FILE)

    all_words = []
    tags = []
    xy = []

    for intent in intents['intents']:
        tag = intent['tag']
        tags.append(tag)

        for pattern in intent['patterns']:
            w = tokenize(pattern)
            all_words.extend(w)
            xy.append((w, tag))

    ignore_words = [',', '?', '/', '.', '!']
    all_words = [stem(w) for w in all_words if w not in ignore_words]
    all_words = sorted(set(all_words))
    tags = sorted(set(tags))

    x_train = []
    y_train = []

    for (pattern_sentence, tag) in xy:
        bag = bag_of_words(pattern_sentence, all_words)
        x_train.append(bag)

        label = tags.index(tag)
        y_train.append(label)

    x_train = np.array(x_train)
    y_train = np.array(y_train)

    num_epochs = 350
    batch_size = 5
    learning_rate = 0.001
    input_size = len(x_train[0])
    hidden_size = 5
    output_size = len(tags)

    dataset = ChatDataset(x_train, y_train)
    train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = NeuralNet(input_size, hidden_size, output_size).to(device=device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=50, gamma=0.5)

    train_model(model, train_loader, num_epochs, criterion, optimizer, scheduler, device)

    data = {
        "model_state": model.state_dict(),
        "input_size": input_size,
        "hidden_size": hidden_size,
        "output_size": output_size,
        "all_words": all_words,
        "tags": tags
    }

    torch.save(data, TRAINED_DATASET_FILE)

    print("Training completed successfully")
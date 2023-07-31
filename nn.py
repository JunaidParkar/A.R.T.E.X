import json
import torch
import torch.nn as nn
import torch.optim as optim
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.model_selection import train_test_split
import torch.nn.functional as F

# Step 1: Load the data from installed_apps_names.json
with open('installed_apps_names.json', 'r') as f:
    app_names = json.load(f)

# Step 2: Preprocess the data
stemmer = PorterStemmer()

def tokenize_and_stem(text):
    tokens = word_tokenize(text.lower())
    return [stemmer.stem(token) for token in tokens]

all_words = set()
app_name_list = []
for app_name in app_names:
    words = tokenize_and_stem(app_name)
    all_words.update(words)
    app_name_list.append((words, app_name))

# Step 3: Prepare data for training
app2label = {app_name: i for i, app_name in enumerate(set(app_names))}

word2index = {word: i for i, word in enumerate(all_words)}
index2word = {i: word for word, i in word2index.items()}

def bag_of_words(tokenized_app_name, word2index):
    bag = [0] * len(word2index)
    for token in tokenized_app_name:
        if token in word2index:
            bag[word2index[token]] += 1
    return bag

X = []
y = []
for (tokenized_app_name, app_name) in app_name_list:
    X.append(bag_of_words(tokenized_app_name, word2index))
    y.append(app2label[app_name])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Define the model
class AppNameClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(AppNameClassifier, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Step 5: Training the model
input_size = len(word2index)
hidden_size = 64  # Increased hidden layer size for better representation
output_size = len(app2label)

model = AppNameClassifier(input_size, hidden_size, output_size)
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

epochs = 300  # Increased number of training epochs
for epoch in range(epochs):
    total_loss = 0
    for i in range(len(X_train)):
        optimizer.zero_grad()
        output = model(torch.tensor(X_train[i], dtype=torch.float).unsqueeze(0))
        target = torch.tensor([y_train[i]], dtype=torch.long)  # Use the category label as the target
        loss = criterion(output, target)
        total_loss += loss.item()
        loss.backward()
        optimizer.step()
    print(f"Epoch: {epoch+1}/{epochs}, Loss: {total_loss/len(X_train):.4f}")

# Compute final loss on test set
with torch.no_grad():
    total_loss = 0
    for i in range(len(X_test)):
        output = model(torch.tensor(X_test[i], dtype=torch.float).unsqueeze(0))
        target = torch.tensor([y_test[i]], dtype=torch.long)  # Use the category label as the target
        loss = criterion(output, target)
        total_loss += loss.item()
    print(f"Final Loss: {total_loss/len(X_test):.4f}")

# Step 6: Save the trained model
torch.save(model.state_dict(), 'app_name_classifier.pth')

# ... (Steps 7 to 9 remain the same)


# Step 7: Load the trained model
model = AppNameClassifier(input_size, hidden_size, output_size)
model.load_state_dict(torch.load('app_name_classifier.pth'))
model.eval()

# Step 8: Recognize app name from user input
def predict_app_name(user_input):
    tokenized_input = tokenize_and_stem(user_input)
    input_bag = bag_of_words(tokenized_input, word2index)
    with torch.no_grad():
        output = model(torch.tensor(input_bag, dtype=torch.float).unsqueeze(0))
    probabilities = F.softmax(output, dim=1)
    predicted_app_index = torch.argmax(probabilities, dim=1).item()
    predicted_app = list(app2label.keys())[list(app2label.values()).index(predicted_app_index)]
    return predicted_app


# Step 9: Test the model
while True:
    user_input = input("Enter the name of the app: ")
    print(f"user_input: {user_input}")
    if user_input == "exit":
        break
    predicted_app = predict_app_name(user_input)
    print(f"Opening {predicted_app}...")

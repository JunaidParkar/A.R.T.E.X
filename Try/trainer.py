import json
import nltk
import pickle

def write_binary_file(data, filename):
    serialized_data = pickle.dumps(data)

    with open(filename, 'wb') as file:
        file.write(serialized_data)

def tokenise(sentence: str):
    return nltk.word_tokenize(sentence)

def train():
    with open("Try/intents.json", "r") as intents:
        intents = json.load(intents)
    intents_array = intents["intents"]
    dataset1 = []
    dataset2 = {}
    for intents in intents_array:
        patterns = intents["patterns"]
        for pattern in patterns:
            tokenised_pattern = tokenise(pattern)
            sets = [intents["tag"], tokenised_pattern]
            dataset1.append(sets)
        responses = intents["responses"]
        dataset2[intents['tag']] = responses
    write_binary_file(dataset1, "db1.bin")
    write_binary_file(dataset2, "db2.bin")
    print(dataset2)

train()
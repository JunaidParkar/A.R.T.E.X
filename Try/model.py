import pickle
import nltk

def tokenise(sentence: str):
    return nltk.word_tokenize(sentence)

def read_binary_file(filename):
    with open(filename, 'rb') as file:
        serialized_data = file.read()
    data = pickle.loads(serialized_data)
    return data


def artex(query: str):
    datasets = read_binary_file("db1.bin")
    responses  = read_binary_file("db2.bin")

    matching = []

    query = tokenise(query)

    for dataset, index in enumerate(datasets):
        print(dataset[1])

artex("hey")
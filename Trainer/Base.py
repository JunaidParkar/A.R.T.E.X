import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer
import pickle

Stemmer = PorterStemmer()

def tokenize(sentence: str):
    return nltk.word_tokenize(sentence)

def stem(word: str):
    return Stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence: list,words: list):
    sentence_word = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words),dtype=np.float32)
    for idx , w in enumerate(words):
        if w in sentence_word:
            bag[idx] = 1
    return bag

def read_binary_file(filename):
    with open(filename, 'rb') as file:
        serialized_data = file.read()
    data = pickle.loads(serialized_data)
    return data
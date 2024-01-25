import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer
import pickle

Stemmer = PorterStemmer()

def tokenize(sentence: str):
    return nltk.word_tokenize(sentence)

def stem(word: str):
    return Stemmer.stem(word.lower())

def read_binary_file(filename):
    with open(filename, 'rb') as file:
        serialized_data = file.read()
    data = pickle.loads(serialized_data)
    return data

def wordPercentageCalculator(query_tokenised: str, responses_filtered: str):
    set1 = set(query_tokenised)
    percentile_list = []
    for response in responses_filtered:
        set2 = set(response[1])
        intersection = len(set2.intersection(set1))
        union = len(set2.union(set1))
        similarity_percentage = (intersection / union) * 100
        percentile_list.append(similarity_percentage)
    if all(num == 0 for num in percentile_list):
        return [-1]
    return percentile_list
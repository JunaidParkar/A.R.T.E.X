import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer

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

def wordsFilter(apps_list: list, query_app: list):
    comm = []
    for index, each_app in enumerate(apps_list):
        wrd = []
        for word in query_app:
            if word.lower() in each_app:
                wrd.append(word)
        comm.append(wrd)
    return comm

def wordPercentageCalculator(tokenised_query: list, filtered_query: list):
    query_length = len(tokenised_query)
    percentile_list = []
    for list in filtered_query:
        list_length = len(list)
        percentage = (list_length / query_length) * 100
        percentile_list.append(percentage)
    if all(num == 0 for num in percentile_list):
        return [-1]
    return percentile_list
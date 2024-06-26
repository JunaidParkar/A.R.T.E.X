import pickle
import random
from nltk.stem.porter import PorterStemmer

temp_model = "temp_model.txt"

class Model():
    
    def __init__(self):
        self.db1 = "intent_quotions.bin"
        self.db2 = "intent_answers.bin"
        self.quotions = []
        self.response = []
        self.stemmer = PorterStemmer()

    def tokenize(self, sentence: str):
        return sentence.split(" ")
    
    def stem(self, sentence: str):
        return self.stemmer.stem(sentence.lower())
    
    def filter_words(self, words: list[any]):
        stop_words = [",", "/", "?", "!", ":", "'", '"', ".", "...", ".."]
        return [word for word in words if word.lower() not in stop_words]

    def loadData(self):
        with open(self.db1, "rb") as db1:
            self.quotions.append(pickle.loads(db1.read()))
            db1.close()
        with open(self.db2, "rb") as db2:
            self.response.append(pickle.loads(db2.read()))
            db2.close()

    def wordPercentageCalculator(self, query_tokenised: str):
        set1 = set(query_tokenised)
        percentile_list = []
        for data in self.quotions[0]:
            set2 = set(data[1])
            intersection = set1.intersection(set2)
            percentile_list.append([(len(intersection) / len(set1)) * 100, data[0]])
        if all(num == 0 for num in percentile_list):
            return [-1]
        return percentile_list

    def getResponse(self, query: str):
        query = [self.stem(wrd) for wrd in self.tokenize(query)]
        print(query)
        filtered_query = self.filter_words(query)
        percentile = self.wordPercentageCalculator(filtered_query)

        if percentile[0] == -1:
            return -1
        max_percentage = max(percentile, key=lambda x: x[0])
        print(max_percentage)
        if max_percentage[0] >= float(75):
            tag = max_percentage[1]
            print(tag)
            response = random.choice(self.response[0][tag])
            print(response)
        else: print(None)

a = Model()
a.loadData()
# a.getResponse("what is the update on weather tomorrow")
a.getResponse("go to sleep")
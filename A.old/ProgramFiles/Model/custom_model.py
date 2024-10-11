import pickle
import random
from nltk.stem.porter import PorterStemmer
from ..EnvPaths import EnvironmentDatabase

class Model():
    
    def __init__(self):
        self.__env = EnvironmentDatabase()
        self.__intent_q = self.__env.get_variable_path("INTENT_QUOTIONS")
        self.__intent_a = self.__env.get_variable_path("INTENT_ANSWERS")
        self.__env.close_connection()

        self.__db1 = self.__intent_q
        self.__db2 = self.__intent_a
        self.__quotions = []
        self.__response = []
        self.__stemmer = PorterStemmer()

    def __tokenize(self, sentence: str):
        return sentence.split(" ")
    
    def __stem(self, sentence: str):
        return self.__stemmer.stem(sentence.lower())
    
    def __filter_words(self, words: list[any]):
        stop_words = [",", "/", "?", "!", ":", "'", '"', ".", "...", ".."]
        return [word for word in words if word.lower() not in stop_words]

    def __loadData(self):
        with open(self.__db1, "rb") as db1:
            self.__quotions.append(pickle.loads(db1.read()))
            db1.close()
        with open(self.__db2, "rb") as db2:
            self.__response.append(pickle.loads(db2.read()))
            db2.close()

    def __wordPercentageCalculator(self, query_tokenised: str):
        set1 = set(query_tokenised)
        percentile_list = []
        for data in self.__quotions[0]:
            set2 = set(data[1])
            intersection = set1.intersection(set2)
            percentile_list.append([(len(intersection) / len(set1)) * 100, data[0]])
        if all(num == 0 for num in percentile_list):
            return [-1]
        return percentile_list

    def getResponse(self, query: str):
        query = [self.__stem(wrd) for wrd in self.__tokenize(query)]
        filtered_query = self.__filter_words(query)
        percentile = self.__wordPercentageCalculator(filtered_query)

        if percentile[0] == -1:
            return None
        max_percentage = max(percentile, key=lambda x: x[0])
        if max_percentage[0] >= float(75):
            tag = max_percentage[1]
            response = random.choice(self.__response[0][tag])
            return response
        else: return None
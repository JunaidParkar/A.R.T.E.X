import json
import pickle
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer


class Trainer():
    def __init__(self, path: str) -> None:
        self.file_path = path
        self.stemmer = PorterStemmer()

    def tokenize(self, sentence: str):
        return word_tokenize(sentence)
    
    def stem(self, sentence: str):
        return self.stemmer.stem(sentence.lower())
    
    def filter_words(self, words: list[any]):
        stop_words = [",", "/", "?", "!", ":", "'", '"', "."]
        return [word for word in words if word.lower() not in stop_words]

    def train(self):
        with open(self.file_path, 'r') as file:
            intents = json.load(file)["intents"]
            db1 = []
            db2 = {}
            for intent in intents:
                for pattern in intent["patterns"]:
                    ps = pattern.split()
                    tw = []
                    for word in ps:
                        tw.append(self.stem(word.lower()))
                    db1.append([intent["tag"], self.filter_words(self.tokenize(" ".join(tw)))])
                db2[intent["tag"]] = intent["responses"]
            
            serialised_data1 = pickle.dumps(db1)
            with open("intent_quotions.bin", "wb") as qb:
                qb.write(serialised_data1)
                qb.close()
            serialised_data2 = pickle.dumps(db2)
            with open("intent_answers.bin", "wb") as qb:
                qb.write(serialised_data2)
                qb.close()
            file.close()

a = Trainer("intents.json")
# print(a.stem("going"))
a.train()
import json
import pickle


class Trainer():
    def __init__(self, path: str) -> None:
        self.file_path = path
        pass

    def train(self):
        with open(self.file_path, 'r') as file:
            intents = json.load(file)["intents"]
            db1 = []
            db2 = {}
            for intent in intents:
                for pattern in intent["patterns"]:
                    db1.append([intent["tag"], pattern])
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

a = Trainer('intents.json')
a.train()
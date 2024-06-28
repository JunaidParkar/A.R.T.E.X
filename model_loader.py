import pickle
from typing import Union

class ModelLoader():
    
    def __init__(self, pth: Union[bool, str] = False) -> None:
        self.db1 = "intent_quotions.bin"
        self.db2 = "intent_answers.bin"
        self.pth = pth
        self.data_to_return = []

    def readData(self):
        if not self.pth:
            with open(self.db1, "rb") as db1:
                self.data_to_return.append(pickle.loads(db1.read()))
                db1.close()
            with open(self.db2, "rb") as db2:
                self.data_to_return.append(pickle.loads(db2.read()))
                db2.close()
        else:
            with open(self.pth, "rb") as pth:
                self.data_to_return.append(pickle.loads(pth.read()))
                pth.close()
        return self.data_to_return

a = ModelLoader()
print(a.readData())
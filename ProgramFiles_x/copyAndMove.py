import shutil
import os

class copyAndMove():
    
    def __init__(self):
        pass
    
    def copy(self, fromPath: str, toPath: str):
        try:
            shutil.copy(src=fromPath, dst=toPath)
            return True
        except Exception as er:
            return er
        
    def move(self, fromPath: str, toPath: str):
        try:
            shutil.move(src=fromPath, dst=toPath)
            return True
        except Exception as er:
            return er
        
a = copyAndMove()
print(a.copy(os.path.join(os.getcwd(), "temp1\\html.html"), os.path.join(os.path.join(os.getcwd(), "temmp"), "inho")))
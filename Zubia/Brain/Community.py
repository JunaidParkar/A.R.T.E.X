import json
import os
import requests
 
def checkInternet():
    try:
        # Send a simple HTTP GET request to a known website (e.g., Google)
        response = requests.get("https://junaidparkar-f7e41.web.app", timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

def handleDirectory(dirPath: str):
    if os.path.isdir(dirPath):
        print("existDir")
    else:
        os.mkdir(dirPath)
        print("dirCreated")

def handleFile(filePath: str):
    if os.path.exists(filePath):
        print("fileExist")
    else:
        with open(filePath, "w") as f:
            f.close()
        print("fileCreated")

def writeDataInFile(data, filename):
    if os.path.exists(filename):
        if os.path.getsize(filename) == 0:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
        else:
            try:
                with open(filename, 'r+') as file:
                    existing_data = json.load(file)
                    existing_data.update(data)
                    file.seek(0)
                    json.dump(existing_data, file, indent=4)
            except:
                with open(filename, 'w') as file:
                    json.dump(data, file, indent=4)
    else:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
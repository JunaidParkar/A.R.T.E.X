
import json
import os
import sys
import datetime
sys.path.append(os.environ.get('Zubia'))
import Setup.Paths as filePaths


def verifyLog():
    if os.path.isfile(filePaths.LOG):
        pass
    else:
        with open(filePaths.LOG, "w") as f:
            f.close()

def writeLogFile(text):
    verifyLog()
    with open(filePaths.LOG, "ab+") as process:
        process.write(f"[{datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}] {text}\n".encode("utf-8"))
        process.close()

def updateCongif(key: str, value: str):
    with open(filePaths.SOFTWARE_CONFIG_FILE, "r+") as f:
        data = json.load(f)
        data[key] = value
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
import eel
from ProgramFiles.sq import AppRegistry
from ProgramFiles.sst import SpeechRecognitionModel, StopRecognition
import threading
import time
import sys

eel.init("./System/Data")

apps = AppRegistry()

def getAllAppsForDisplay():
    app_list = apps.get_allApps()
    print(app_list)

def run_sst():
    try:
        SpeechRecognitionModel()
    except Exception as e:
        print(f"Error in SST thread: {e}")

@eel.expose
def closeApp():
    StopRecognition()
    sst_thread
    sys.exit()

if __name__ == "__main__":
    sst_thread = threading.Thread(target=run_sst)

    sst_thread.start()
    eel.start("artex.ui/index.html")
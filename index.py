import eel
from ProgramFiles.sq import AppRegistry
from ProgramFiles.sst import SpeechRecognitionModel
import threading
import time

eel.init("./System/Data")

apps = AppRegistry()

def getAllAppsForDisplay():
    app_list = apps.get_allApps()
    print(app_list)

# allApps = getAllAppsForDisplay()

def startApp():
    eel.start("artex.ui/index.html")

if __name__ == "__main__":
    # Run Eel in a separate thread
    gui_thread = threading.Thread(target=startApp)
    sst_thread = threading.Thread(target=SpeechRecognitionModel)
    print("Eel window started in a separate thread")
    gui_thread.start()
    sst_thread.start()
    # Main thread continues to run other tasks if needed
    while True:
        time.sleep(1)
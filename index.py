from ProgramFiles import Speaker, EnvironmentDatabase, Model, LogWritter



import eel
# from ProgramFiles.sq import AppRegistry
# from ProgramFiles.sst import SpeechRecognitionModel, StopRecognition
import threading
import time
import sys

# eel.init("./System/Data")

# apps = AppRegistry()

# def getAllAppsForDisplay():
#     app_list = apps.get_allApps()
#     print(app_list)

# def run_sst():
#     try:
#         SpeechRecognitionModel()
#     except Exception as e:
#         print(f"Error in SST thread: {e}")

# @eel.expose
# def closeApp():
#     StopRecognition()
#     sst_thread
#     sys.exit()
if __name__ == "__main__":
    # sst_thread = threading.Thread(target=run_sst)

    # sst_thread.start()
    # eel.start("artex.ui/index.html")
    # speak()
    # env = EnvironmentDatabase()
    # env.create_variable("Intent_quotions", r"C:\Users\verix\Documents\xampp\htdocs\A.R.T.E.X\System\Community\intent_quotions.bin")
    # env.create_variable("Intent_answers", r"C:\Users\verix\Documents\xampp\htdocs\A.R.T.E.X\System\Community\intent_answers.bin")
    # env.close_connection()
    # ar = Model()
    # ar.loadData()
    # print(ar.getResponse("hello"))
    l = LogWritter("hy.txt")
    print(l.__fileName)
    pass
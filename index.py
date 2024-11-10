import os       
from ProgramFiles import Initialization

app_log_file = os.path.join(os.getcwd(), "System", "Logs", "app.log")

if not os.path.isdir(os.path.join(os.getcwd(), "System")):
    os.mkdir(os.path.join(os.getcwd(), "System"))
if not os.path.isdir(os.path.join(os.getcwd(), "System", "Logs")):
    os.mkdir(os.path.join(os.getcwd(), "System", "Logs"))

a = Initialization(app_log_file)
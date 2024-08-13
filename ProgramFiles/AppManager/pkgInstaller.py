import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import json
from EnvPaths.editor import EnvironmentDatabase
from Zipper.z import unzip_folder
# print(str(Path(__file__).parent.parent))

class Installer:

    def __init__(self) -> None:
        self.env = EnvironmentDatabase()

    def install(self, pkg):
        if os.path.isfile(os.path.join(self.env.get_variable_path("APP_DOWNLOAD_PATH"), f"{pkg}.zip")):
            # unzip_folder(os.path.join(self.env.get_variable_path("APP_DOWNLOAD_PATH"), f"{pkg}.zip"), r"C:\Users\verix\Documents\xampp\htdocs\A.R.T.E.X\System\Data", b"fn89wrehi38r38ryhd")
            print(os.path.join(self.env.get_variable_path("APP_DATA"), pkg, "config.json"))
            with open(os.path.join(self.env.get_variable_path("APP_DATA"), pkg, "config.json"), "r") as cj:
                config = json.load(cj)
                cj.close()
                print(config)
            print("app installed successfully")
        else:
            print("installer not found")


a = Installer()
a.install("artex.iu")
# b = EnvironmentDatabase()
# b.create_variable("APP_DATA", r"C:\Users\verix\Documents\xampp\htdocs\A.R.T.E.X\System\Data")
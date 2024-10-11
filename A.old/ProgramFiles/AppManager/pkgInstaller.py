import os
import sys
import json
import shutil
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from EnvPaths.editor import EnvironmentDatabase
from AppManager.registry import AppRegistry
from ProgramFiles.Zipper.zip import unzip_folder

class pkgManager:
    def __init__(self) -> None:
        self.__env = EnvironmentDatabase()
        self.__app_registry = AppRegistry()
        print("init")

    def install(self, pkg: str, default=0):

        if os.path.isdir(os.path.join(self.__env.get_variable_path("APP_DATA"), pkg)):
            print("app already present")
            return
        
        if os.path.isfile(os.path.join(self.__env.get_variable_path("APP_DOWNLOAD_PATH"), f"{pkg}.zip")):
            uz1 = unzip_folder(os.path.join(self.__env.get_variable_path("APP_DOWNLOAD_PATH"), f"{pkg}.zip"), self.__env.get_variable_path("APP_DATA"), b"fn89wrehi38r38ryhd")
            if uz1[0]:
                if not os.path.isfile(os.path.join(self.__env.get_variable_path("APP_DATA"), pkg, "config.json")):
                    print("config.json not found")
                    shutil.rmtree(os.path.join(self.__env.get_variable_path("APP_DATA"), pkg))
                    return
                with open(os.path.join(self.__env.get_variable_path("APP_DATA"), pkg, "config.json"), "r") as config_file:
                    config = json.load(config_file)
                    config_file.close()
                if os.path.isfile(os.path.join(self.__env.get_variable_path("APP_DATA"), pkg, "assets.zip")):
                    uz2 = unzip_folder(os.path.join(self.__env.get_variable_path("APP_DATA"), pkg, "assets.zip"), os.path.join(self.__env.get_variable_path("APP_DATA"), pkg), b"ARTex101@5765buty6u$^&%Tguyhn675y75rt6rr53145ee67uhyi7786u875tyhy5325r")
                    if uz2[0]:    
                        os.system(f'attrib +h {os.path.join(self.__env.get_variable_path("APP_DATA"), pkg, "assets")}')
                        print(("app installed"))
                        self.__app_registry.register_app(config["name"], config["packageName"], config["version"], default)
                    else: 
                        print(uz2[1])
                        shutil.rmtree(os.path.join(self.__env.get_variable_path("APP_DATA"), pkg))
                else: 
                    self.__app_registry.register_app(config["name"], config["packageName"], config["version"], default)
                    print(("app installed"))
            else: print(uz1[1])
        else: print("installer not found")


    def uninstall(self, pkg: str):
        if os.path.isdir(os.path.join(self.__env.get_variable_path("APP_DATA"), pkg)):
            shutil.rmtree(os.path.join(self.__env.get_variable_path("APP_DATA"), pkg))
            self.__app_registry.delete_app(pkg)
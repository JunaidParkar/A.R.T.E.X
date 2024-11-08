import os
from .. import StampLogger

class Initialization:

    def __init__(self):
        self.__appdata_root = os.path.join(os.getenv("LOCALAPPDATA"), "artex")
        if not os.path.isdir(self.__appdata_root):
            os.mkdir(self.__appdata_root)
        if not os.path.isdir(os.path.join(self.__appdata_root, "system")):
            os.mkdir(os.path.join(self.__appdata_root, "system"))
        if not os.path.isdir(os.path.join(self.__appdata_root, "system", "apps")):
            os.mkdir(os.path.join(self.__appdata_root, "system", "apps"))
            os.system(f'attrib +h "{os.path.join(self.__appdata_root, "system", "apps")}"')
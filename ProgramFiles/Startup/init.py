import os
import logging

class Initialization:

    def __init__(self, log_file):
        self.logging = logging
        self.logging.basicConfig(
            filename=log_file,
            level=self.logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        self.__appdata_root = os.path.join(os.getenv("LOCALAPPDATA"), "artex")
    
    def initDirs(self):
        self.logging.info("\n\nStarting initialization checkup\n\n")
        if not os.path.isdir(self.__appdata_root):
            self.logging.warning(f"\n App data directory not available at {self.__appdata_root}")
            os.mkdir(self.__appdata_root)
            self.logging.info(f"Made directory {self.__appdata_root}")

        if not os.path.isdir(os.path.join(self.__appdata_root, "system")):
            self.logging.warning(f"\nDirectory not available {os.path.join(self.__appdata_root, "system")}")
            os.mkdir(os.path.join(self.__appdata_root, "system"))
            self.logging.info(f"Made directory {os.path.join(self.__appdata_root, "system")}")

        if not os.path.isdir(os.path.join(self.__appdata_root, "system", "apps")):
            self.logging.warning(f"\nDirectory not available {os.path.join(self.__appdata_root, "system", "apps")}")
            os.mkdir(os.path.join(self.__appdata_root, "system", "apps"))
            self.logging.info(f"Made directory {os.path.join(self.__appdata_root, "system", "apps")}")
            self.logging.info("\nHiding directory for apps")
            try:
                os.system(f'attrib +h "{os.path.join(self.__appdata_root, "system", "apps")}"')
                self.logging.info("App directory hidden")
            except Exception as e:
                self.logging.fatal(f"Unable to hide directory with error {e}")
                return {"error": True, "msg": f"Unable to hide directory with error {e}"}

        
        self.logging.info("\nInitialization completed succesfully\n")
        return {"error": False, "msg": "Directory created successfully"}
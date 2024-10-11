import os
import datetime

class StampLogger:

    def __init__(self, log_file):
        self.__log_file = log_file
        if not os.path.isdir(os.path.abspath(os.path.join(self.__log_file, ".."))):
            os.mkdir(os.path.abspath(os.path.join(self.__log_file, "..")))
        if not os.path.isfile(self.__log_file):
            with open(self.__log_file, "w+") as a:
                a.close()

    def write_log(self, stamp):
        log_stamp = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}   {stamp}"
        with open(self.__log_file, "a+") as f:
            f.seek(0, os.SEEK_END)
            if f.tell() > 0:
                f.write("\n")
            f.write(log_stamp)
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from mtranslate import translate
from ..EnvPaths import EnvironmentDatabase


class QR():

    def __init__(self):
        # self.__env = EnvironmentDatabase()
        # self.__html = self.__env.get_variable_path("TTS_HTML")
        # self.__initiator = self.__env.get_variable_path("TTS_Initiator")
        # self.__data_file = self.__env.get_variable_path("TTS_Data")
        # self.__env.close_connection()

        self.__chrome_options = Options()
        self.__user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36"
        self.__chrome_options.add_argument(f'user-agent={self.__user_agent}')
        self.__chrome_options.add_argument("--use-fake-ui-for-media-stream")
        self.__chrome_options.add_argument("--use-fake-device-for-media-stream")
        # self.__chrome_options.add_argument("--headless=new")
        self.__service = Service(ChromeDriverManager().install())
        self.__driver = webdriver.Chrome(service=self.__service, options=self.__chrome_options)
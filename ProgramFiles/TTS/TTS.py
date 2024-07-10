from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from mtranslate import translate
from ..EnvPaths import EnvironmentDatabase


class Speaker():

    def __init__(self):
        self.__env = EnvironmentDatabase()
        self.__html = self.__env.get_variable_path("TTS_HTML")
        self.__initiator = self.__env.get_variable_path("TTS_Initiator")
        self.__data_file = self.__env.get_variable_path("TTS_Data")
        self.__env.close_connection()

        self.__chrome_options = Options()
        self.__user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36"
        self.__chrome_options.add_argument(f'user-agent={self.__user_agent}')
        self.__chrome_options.add_argument("--use-fake-ui-for-media-stream")
        self.__chrome_options.add_argument("--use-fake-device-for-media-stream")
        self.__chrome_options.add_argument("--headless=new")
        self.__service = Service(ChromeDriverManager().install())
        self.__driver = webdriver.Chrome(service=self.__service, options=self.__chrome_options)

        self.__current_voice = "Googel UK English Male (en-GB)"

    def __translate_to(self, text):
        return translate(text, "en-us")
    
    def __initiate_speak(self):
        with open(self.__initiator, "w") as initiator_file:
            initiator_file.write("A")

    def quit_speak(self):
        with open(self.__initiator, "w") as initiator_file:
            initiator_file.write("B")
        self.__driver.quit()

    def speak(self):
          self.__initiate_speak()
          self.__driver.get(self.__html)
          previous_text = None
          while True:
            with open(self.__initiator, "a+") as initiator_file:
                initiator_file.seek(0)
                to_speak = initiator_file.read()
                initiator_file.close()
            if not to_speak == "A":
                break
            with open(self.__data_file, "a+") as data_file:
                data_file.seek(0)
                data = data_file.read()
                data_file.close()
            if previous_text != data:
                previous_text = data
                translated_text = self.__translate_to(data)
                input_btn = self.__driver.find_element(By.ID, "text-to-speak")
                start_btn = self.__driver.find_element(By.ID, "start-speech")
                input_btn.clear()
                input_btn.send_keys(translated_text)
                start_btn.click()
            sleep(0.33)
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
        self.env = EnvironmentDatabase()
        self.html = self.env.get_variable_path("TTS_HTML")
        self.initiator = self.env.get_variable_path("TTS_Initiator")
        self.data_file = self.env.get_variable_path("TTS_Data")
        self.env.close_connection()

        self.chrome_options = Options()
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36"
        self.chrome_options.add_argument(f'user-agent={self.user_agent}')
        self.chrome_options.add_argument("--use-fake-ui-for-media-stream")
        self.chrome_options.add_argument("--use-fake-device-for-media-stream")
        self.chrome_options.add_argument("--headless=new")
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)

        self.current_voice = "Googel UK English Male (en-GB)"

    def __translate_to(self, text):
        return translate(text, "en-us")
    
    def __initiate_speak(self):
        with open(self.initiator, "w") as initiator_file:
            initiator_file.write("A")

    def quit_speak(self):
        with open(self.initiator, "w") as initiator_file:
            initiator_file.write("B")
        self.driver.quit()

    def speak(self):
          self.__initiate_speak()
          self.driver.get(self.html)
          previous_text = None
          while True:
            with open(self.initiator, "a+") as initiator_file:
                initiator_file.seek(0)
                to_speak = initiator_file.read()
                initiator_file.close()
            if not to_speak == "A":
                break
            with open(self.data_file, "a+") as data_file:
                data_file.seek(0)
                data = data_file.read()
                data_file.close()
            if previous_text != data:
                previous_text = data
                translated_text = self.__translate_to(data)
                input_btn = self.driver.find_element(By.ID, "text-to-speak")
                start_btn = self.driver.find_element(By.ID, "start-speech")
                input_btn.clear()
                input_btn.send_keys(translated_text)
                start_btn.click()
            sleep(0.33)
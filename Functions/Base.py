import pyttsx3
import json
from Variables.Envirenments import SETTING_CONFIGURATIONS
import bs4 as BeautifulSoup

def remove_markdown(text):

    # Use BeautifulSoup to extract plain text
    soup = BeautifulSoup.BeautifulSoup(text, 'html.parser')
    plain_text = soup.get_text()

    return plain_text

def speak(text):
    text = remove_markdown(text)
    with open(SETTING_CONFIGURATIONS, 'r') as setting:
        voice_conf = json.load(setting)['text-to-speech']
    engine = pyttsx3.init()
    engine.setProperty("voices", engine.getProperty('voices')[voice_conf['voice']])
    engine.setProperty('rate', voice_conf['rate'])  # Adjust speaking rate for clarity
    engine.setProperty('volume', 1.0)  # Ensure full volume for better understanding
    engine.setProperty('voice', voice_conf['language'])
    engine.say(text=text)
    engine.runAndWait()
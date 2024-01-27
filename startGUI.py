import eel
import markdown
from markdown.extensions.fenced_code import FencedCodeExtension
from NeuralNetwork.Palm import chatBot
from Functions.Base import speak

eel.init("Systems/GUI")

def convertHTML(msg):
    return markdown.markdown(msg, extensions=[FencedCodeExtension()])

@eel.expose
def getResponse(query):
    bot = chatBot(query)
    print(f"resp: {bot}")
    if bot == None:
        bot = "Unable to process your query at the moment. I am still learning and trying to upgrade myself. I hopy you will bare me a little."
    response = convertHTML(bot)
    return response

@eel.expose
def say(text):
    speak(text)
    return None

eel.start("index.html")
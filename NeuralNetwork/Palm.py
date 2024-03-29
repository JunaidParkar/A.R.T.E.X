import google.generativeai as palm
import json
from Variables.Envirenments import SETTING_CONFIGURATIONS
# import Management.Paths.DataPath as Filepaths

with open(SETTING_CONFIGURATIONS, "r") as fpp:
  api = json.load(fpp)["google-ai"]
  fpp.close()

palm.configure(api_key=api)

# def saveChats(conv):
#   with open(Filepaths.CHAT_DATA_FILE, 'w') as f:
#     json.dump(conv, f, indent=4)
#     f.close()

# def loadChats():
#   try:
#     with open(Filepaths.CHAT_DATA_FILE, 'r') as f:
#       data = json.load(f)
#       f.close()
#       return data
#   except:
#     return []

examples = [
    ("Who are you?",
     "I am an evolutional AI your personal virtual assistant created by MR. Junaid Pakar."
     ),
     ("Who created you?",
      "All credit goes to MR. Junaid Parkar. I am originated by him."),
    ("What can you do?",
     "You can use me for research purposes. I can answer all your questions as I am learning all the latest data. I can set you a reminder for your tasks. And many more things...")
]

defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.9,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}

context = "Be my friend and stay with me"
# messages = loadChats()

def chatBot(input):
  try:
    # query = input
    # tempMsg = messages.copy()
    # tempMsg.append(query)
    response = palm.chat(
      **defaults,
    #   examples=examples,
      prompt=input
    #   messages=tempMsg
    )
    # if response.last is not None:
    #   messages.append(query)
    #   messages.append(response.last)
    #   tempMsg = []
    # saveChats(messages)
    return response.last
  except Exception as e:
    return f"An error occured: {e}"
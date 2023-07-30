import google.generativeai as palm
import json
import Zubia.Brain.Paths as Filepaths

with open(Filepaths.LOCALDATA_CONFIG_FILE, "r") as fpp:
  api = json.load(fpp)["googleAI"]
  fpp.close()

palm.configure(api_key=api)

def saveChats(conv):
  with open(Filepaths.CHAT_DATA_FILE, 'w') as f:
    json.dump(conv, f, indent=4)
    f.close()

def loadChats():
  try:
    with open(Filepaths.CHAT_DATA_FILE, 'r') as f:
      data = json.load(f)
      f.close()
      return data
  except:
    return []

examples = [
    ("Who are you?",
     "I am Zubia your personal AI assistant created by MR. Junaid Pakar."
     ),
     ("Who created you?",
      "All credit goes to MR. Junaid Parkar. I am originated by him.")
]

defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.9,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}

context = "Be my friend and stay with me"
messages = loadChats()

def chatBot(input):
  query = input
  tempMsg = messages.copy()
  tempMsg.append(query)
  response = palm.chat(
    **defaults,
    context=context,
    examples=examples,
    messages=tempMsg
  )
  if response.last is not None:
    messages.append(query)
    messages.append(response.last)
    tempMsg = []
  saveChats(messages)
  return response.last
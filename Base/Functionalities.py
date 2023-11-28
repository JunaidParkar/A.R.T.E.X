import speech_recognition as sr
import pyttsx3

def listen():
    r = sr.Recognizer()
    r.energy_threshold = 4000
    with sr.Microphone() as source:
        print("Listening")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        print("Speak Anything :")
        audio = r.listen(source, 0, 8)
        try:
            print("recognizing")
            text = r.recognize_google(audio, "en-hi")
            print("You said : {}".format(text))
            print(text)
            return text.lower()
        except:
            print("Error")
            return "Error"

# listen()

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("voices", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0 Microsoft David Desktop - English (United States)")
    engine.setProperty("rate", 150)
    engine.say(text=text)
    engine.runAndWait()

def main():
    txt = listen()
    speak(txt)

# main()

def getVoices():
    eng = pyttsx3.init()
    voices = eng.getProperty("voices")

    for ind, voice in enumerate(voices):
        print(ind, voice.id, voice.name)

# getVoices()

# speak("Hello sir, My name is ARTEX your personal AI assistant")

# Save binary data to a file
# Save binary data to a file
# with open('file.bin', 'w') as file:
#     data = bin(12345)  # This is a binary string
#     file.write(data)


# Read binary data from a file
# Read binary data from a file
# Read binary data from a file
# with open('file.bin', 'r') as file:
#     data = file.read()
#     number = int(data, 2)  # Convert binary string to integer
#     print(number)

import json
import pickle

# Some JSON data
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Convert the data to a JSON string
json_data = json.dumps(data)

# Convert the JSON string to bytes
bytes_data = json_data.encode()

# Write the bytes to a file
with open('file.bin', 'wb') as file:
    pickle.dump(bytes_data, file)

# import json
# import pickle

# Read the bytes from the file
with open('file.bin', 'rb') as file:
    bytes_data = pickle.load(file)

# Convert the bytes to a JSON string
json_data = bytes_data.decode()

# Convert the JSON string to data
data = json.loads(json_data)

print(data)

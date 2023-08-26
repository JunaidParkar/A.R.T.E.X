import webbrowser
import os
import sys
sys.path.append(os.environ.get('EvoAI'))
from Evo.Body.Mouth import speak
from urlextract import URLExtract

def visitWebsite(query: str):
    removableQuery = ["visit", "website", "open", "start", "launch"]
    extractor = URLExtract()
    urls = extractor.find_urls(query)
    if urls:
        speak(f"visiting {urls[0]}")
        webbrowser.open(urls[0])
    else:
        for word in removableQuery:
            query = query.replace(word, "")
        speak(f"Performing a regular search for '{query}'...")
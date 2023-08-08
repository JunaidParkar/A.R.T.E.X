import webbrowser
import os
import sys
sys.path.append(os.environ.get('Zubia'))
from Zubia.Body.Mouth import speak
from urlextract import URLExtract
from selenium import webdriver

def visitWebsite(query):
    removableQuery = ["visit", "website", "open", "start", "launch"]
    extractor = URLExtract()
    urls = extractor.find_urls(query)
    if urls:
        # If URLs are found, open the first URL in the default web browser
        speak(f"visiting {urls[0]}")
        webbrowser.open(urls[0])
    else:
        for word in removableQuery:
            query = query.replace(word, "")
        speak(f"Performing a regular search for '{query}'...")
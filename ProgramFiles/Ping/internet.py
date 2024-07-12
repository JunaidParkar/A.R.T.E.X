import requests

def checkConnection(url="https://google.com", timeout=5):
    try:
        response = requests.get(url=url, timeout=timeout)
        return response.status_code >= 200 and response.status_code <= 300
    except:
        return False
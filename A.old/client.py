import requests
import json

# URL to send the POST request to
url = 'http://localhost:3000/generateResponse'

# Data to be sent in the POST request
data = {
    'prompt': 'Hello dear write me a poem on rain'
}

# Headers to be sent in the POST request
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
}

# Send the POST request with data and headers
response = requests.post(url, data=json.dumps(data), headers=headers)

# Print the response status code and content
print(f'Status Code: {response.status_code}')
print(f'Response Content: {response.text}')

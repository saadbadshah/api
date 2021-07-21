import requests

TARGET_URL = "http://127.0.0.1:5000/"

response = requests.get(TARGET_URL + "Validate/978-0-262-13472-9")
print (response.text)
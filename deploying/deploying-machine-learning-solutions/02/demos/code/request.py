import requests

url = 'http://localhost:8080/api'
r = requests.post(url, json = {"x" : ['I Love U']})
print(r.json())
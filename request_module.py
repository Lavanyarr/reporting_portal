import requests

# login
data = '{"username": "mohana", "password": "krish"}'
url = 'http://localhost:8080/api/gyaan_auth/login/v1/'
headers={"Content-type": "application/json"}
response = requests.post(url=url, data=data, headers=headers)
print(response.content)


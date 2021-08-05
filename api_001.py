import requests

res = requests.get('https://api.github.com/users/soongon')
print(res.json())

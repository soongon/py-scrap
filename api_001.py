import requests

res = requests.get('https://api.github.com/users/soongon')
soongon = res.json()

print(soongon['html_url'])


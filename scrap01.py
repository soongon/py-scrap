import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.daum.net/')
soup = BeautifulSoup(res.text, 'html.parser')

the_tag = soup.select_one('#cSub > div > ul > li:nth-child(1) > div.item_issue > div > strong > a')

print(the_tag.text)


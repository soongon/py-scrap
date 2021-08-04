import requests
from bs4 import BeautifulSoup

res = requests.get('https://finance.daum.net/')
soup = BeautifulSoup(res.text, 'html.parser')
the_tag = soup.select_one('#boxIndexes')
print(the_tag)
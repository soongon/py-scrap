import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.yes24.com/24/Category/BestSeller')
soup = BeautifulSoup(res.text, 'html.parser')
the_tag = soup.select_one('#bestList > ol > li.num1 > p:nth-child(3) > a')
print(the_tag.text)
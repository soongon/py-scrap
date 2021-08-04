import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

res = requests.get('https://www.coupang.com/np/campaigns/82/components/194176', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
the_tag = soup.select_one('#productList > li:nth-child(1) > a > dl > dd > div.name')
print(the_tag.text)

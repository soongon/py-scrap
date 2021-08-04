import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

res = requests.get('https://www.coupang.com/np/categories/393760', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

li_tags = soup.select('#productList > li')

# for coupang products
product_list = []

for li_tag in li_tags:
    print(li_tag.select_one('a > dl > dd > div.name').text.strip())
    # 가격 print(...)
    # 좋아요 갯수 print(...)
    # 이미지 URL print(...)
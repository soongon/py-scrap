import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

res = requests.get('https://www.coupang.com/np/campaigns/82/components/194176', headers=headers)
print(res.text)


# 쿠팡의 로켓배송 -> 식품 -> 첫번째 상품의 이름 출력
# 멜론사이트 -> 차트 -> 1등곡명, 가수명, 앨범명 출력

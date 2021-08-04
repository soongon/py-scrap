import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

title = ''
singer = ''
album_title = ''

res = requests.get('https://www.melon.com/chart/index.htm', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

title_tag = soup.select_one('#frm > div > table > tbody > tr:nth-child(1) > td:nth-child(4) > div > div > div.ellipsis.rank01 > span > a')
title = title_tag.text

singer_tag = soup.select_one('#frm > div > table > tbody > tr:nth-child(1) > td:nth-child(4) > div > div > div.ellipsis.rank02 > a')
singer = singer_tag.text

album_title_tag = soup.select_one('#frm > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > div > div > div > a')
album_title = album_title_tag.text

print('멜론 1위 곡 ' + album_title + '앨범의 ' + singer + '의 ' + title + '입니다.')


# 쿠팡의 로켓배송 -> 식품 -> 첫번째 상품의 이름 출력
# 멜론사이트 -> 차트 -> 1등곡명, 가수명, 앨범명 출력

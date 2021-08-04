import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

res = requests.get('https://www.melon.com/chart/index.htm', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

tr_tags = soup.select('#frm > div > table > tbody > tr')

# for melong songs
song_list = []

for tr_tag in tr_tags:
    song_list.append([
        tr_tag.select_one('td:nth-child(4) > div > div > div.ellipsis.rank01 > span > a').text,  # 곡명
        tr_tag.select_one('').text,  # 가수명
        tr_tag.select_one('').text,  # 앨범명
        tr_tag.select_one('').text,  # 앨범 이미지 URL
    ])

print(song_list)

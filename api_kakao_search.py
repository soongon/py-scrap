import requests
import pprint

headers = {
    'Authorization': 'KakaoAK ecac015e337f78c1e011261e4ffa851a'
}
params = {
    'query': '올림픽'
}
res = requests.get('https://dapi.kakao.com/v2/search/web', headers=headers, params=params)
# pprint.pprint(res.json()['documents'])

for item in res.json()['documents']:
    print(item['title'].replace('<b>', '').replace('</b>', ''))

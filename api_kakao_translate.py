import requests
import pprint

headers = {
    'Authorization': 'KakaoAK ecac015e337f78c1e011261e4ffa851a'
}
params = {
    'query': '문장 번역요청한 문장을 다양한 언어로 번역하는 API로써 입력된 텍스트를 기반으로 번역 텍스트 결과를 전달합니다. 한국어와 타언어간 번역외에도 타언어간 번역도 지원됩니다.',
    'src_lang': 'kr',
    'target_lang': 'en'
}
res = requests.get('https://dapi.kakao.com/v2/translation/translate', headers=headers, params=params)
# pprint.pprint(res.json())

print(res.json()['translated_text'][0][0])

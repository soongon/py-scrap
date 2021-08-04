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
    image_url = 'http:' + li_tag.select_one('a > dl > dt > img')['src']
    product_list.append([
        li_tag.select_one('a > dl > dd > div.name').text.strip(),
        int(li_tag.select_one('a > dl > dd > div.price-area > div > div.price > em > strong').text.replace(',', '')),
        int(li_tag.select_one('a > dl > dd > div.other-info > div > span.rating-total-count').text[1:-1]),
        image_url,
    ])

    img_res = requests.get(image_url)
    filename = image_url[image_url.rindex('/') + 1:]
    with open('./coupang_img/' + filename, 'wb') as f:
        f.write(img_res.content)
        print(filename + ' 파일 쓰기완료')

print(product_list)

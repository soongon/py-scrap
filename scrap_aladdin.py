import requests
from bs4 import BeautifulSoup

# 1. 해당 화면의 HTML 을 가져온다.
res = requests.get('https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&start=we')

# 2. HTML을 Beautifulsoup을 써서 파서블한 HTML로 변환
soup = BeautifulSoup(res.text, 'html.parser')

# 3. 타겟 태그의 CSS Selector 를 확보한다.
the_tag = soup.select_one('#Myform > div:nth-child(3) > table > tr > td:nth-child(3) > table > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li:nth-child(2) > a.bo3 > b')
print(the_tag.text)

#Myform > div:nth-child(3) > table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li:nth-child(2) > a.bo3 > b

# 실습과제 : yes24 베스트셀러 1위 책제목 출력
# 다음 증권 사이트의 현재 코스피 지수

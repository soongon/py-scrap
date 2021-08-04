import requests
from bs4 import BeautifulSoup


def get_html_from_url(url='http://www.naver.com'):
    return requests.get(url)


def main():
    res = get_html_from_url(url='http://daum.net')
    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup)


main()

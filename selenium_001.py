from selenium import webdriver
import time
from bs4 import BeautifulSoup

browser = webdriver.Chrome('./chromedriver')

browser.get('https://www.daum.net/')
time.sleep(3)

browser.find_element_by_css_selector('#gnbServiceList > ul > li:nth-child(5) > a').click()
time.sleep(2)

target_html = browser.page_source
browser.close()

soup = BeautifulSoup(target_html, 'html.parser')
the_tag = soup.select_one('#boxIndexes > div:nth-child(1) > span.num.up > strong')
print(the_tag.text)

from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')

browser = webdriver.Chrome('./chromedriver', options=options)

browser.get('http://www.naver.com')
print('네이버로 이동')
time.sleep(5)
browser.get_screenshot_as_file('naver.png')
print('screen shot ok..')
browser.close()

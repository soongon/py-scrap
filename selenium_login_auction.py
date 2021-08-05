# for secret
PW = ''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from bs4 import BeautifulSoup

browser = webdriver.Chrome('./chromedriver')
browser.get('http://www.auction.co.kr/')
time.sleep(2)

browser.find_element(By.CSS_SELECTOR, '#headerloginveiw > a').click()
time.sleep(2)

browser.find_element(By.ID, 'id').send_keys('luxclinic', Keys.TAB, PW, Keys.ENTER)
time.sleep(2)

browser.get('https://memberssl.auction.co.kr/Myauction/default.aspx?frm=hometab')
time.sleep(2)

target_html = browser.page_source
# browser.find_element(By.ID, 'id').send_keys('luxclinic')
# time.sleep(0.5)
# browser.find_element(By.ID, 'password').send_keys(PW)
# time.sleep(0.2)
# browser.find_element(By.XPATH, '//*[@id="login-app"]/div/div[1]/fieldset/button[1]').click()
browser.close()

soup = BeautifulSoup(target_html, 'html.parser')

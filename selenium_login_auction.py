from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('./chromedriver')
browser.get('http://www.auction.co.kr/')
time.sleep(2)

browser.find_element(By.CSS_SELECTOR, '#headerloginveiw > a').click()
time.sleep(2)

# browser.find_element(By.ID, 'id')\
#     .send_keys('soongon', Keys.TAB, 'abcdedfd', Keys.ENTER)

browser.find_element(By.ID, 'id').send_keys('soongon')
time.sleep(0.5)
browser.find_element(By.ID, 'password').send_keys('sldkfjdlskfjdklsfj')
time.sleep(0.2)
browser.find_element(By.XPATH, '//*[@id="login-app"]/div/div[1]/fieldset/button[1]').click()


time.sleep(5)
browser.close()

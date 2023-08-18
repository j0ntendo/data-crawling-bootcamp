import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

url = f"https://play.google.com/store/apps/details?id=com.sampleapp&hl=ko-KR"
print(url)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
driver.maximize_window()
time.sleep(3)
# driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
# driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
# driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
# driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
# driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
# time.sleep(1)
test1 = '#yDmH0d > c-wiz.SSPGKf.Czez9d > div > div > div.tU8Y5c > div.wkMJlb.YWi3ub > div > div.qZmL0 > div:nth-child(1) > c-wiz:nth-child(4) > section > header > div > div:nth-child(2) > button'
driver.find_element(By.CSS_SELECTOR, test1).click()
time.sleep(1)
popup = driver.find_element(By.CLASS_NAME, 'fysCi')
popup.click()

prev_count = 0
new_count = 0

while True:
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(2)
    new_count = len(driver.find_elements(By.CLASS_NAME, 'h3YV2d'))
    if new_count == prev_count or new_count >= 1000:
        break

    prev_count = new_count
stars = driver.find_elements(By.CLASS_NAME, 'iXRFPc')
reviws = driver.find_elements(By.CLASS_NAME, 'h3YV2d')

review_list = []
for temp in reviws:
    review_list.append(temp.text)

star_list = []
for temp in stars:
    temp = temp.get_attribute('aria-label')
    temp = temp.replace('별표 5개 만점에 ', '')
    temp = temp[0]
    star_list.append(temp)

data = {}
data['text'] = review_list
data['score'] = star_list
pd.DataFrame(data).to_csv('bae_review.csv', encoding='utf-8')
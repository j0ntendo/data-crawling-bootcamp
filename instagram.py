import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

url = f"https://www.instagram.com/"
print(url)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
driver.maximize_window()
time.sleep(3)


keyword = '연세대학교'
max_comment = 2
login_id = 'jonnyjonyyespapa'
login_pw = 'Jesusteama1_'

driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(login_id)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(login_pw)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
time.sleep(3)

driver.get(f'https://www.instagram.com/explore/tags/{keyword}')
time.sleep(10)

driver.find_elements(By.CSS_SELECTOR, 'div._aagw')[0].click()
time.sleep(3)

result = []
count = 0
while len(result) < max_comment:
    while True:
        driver.find_element(By.CSS_SELECTOR,'ul._a9z6._a9za').click()
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.End)
        plus_button = driver.find_elements(By.CSS_SELECTOR, 'ul._a9z6._a9za > li > div > button._abl-').click()

        if len(plus_button) > 0:
            plus_button[0].click()
            time.sleep(1)

        else:
            break

    comments = driver.find_elements(By.CSS_SELECTOR,'span._aacl._aaco._aacu._aacx._aad7._aade')
    temp_list = []
    for r in comments:
        temp_list.append(r.text)

    result.append({'reply': temp_list}) # if there are 100 comments then 100 lists created
    count += 1

    df = pd.DataFrame.from_dict(data=result, orient='columns')
    df.to_csv("insta.csv", mode = 'a', header=False)

    try:
        #driver.find_element(By.XPATH, ''
        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.ARROW_RIGHT)
    except:
        break

# i installed webdriver_manager, selenium, pandas, bs4

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

# get the url
keyword = '연세대학교'
url = f"https://www.youtube.com/results?search_query={keyword}"

# opening the chrome window
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True) # prevents the website from crashing
driver = webdriver.Chrome(options=chrome_options) # install chrome drive manager
driver.get(url)
driver.maximize_window()  # open the browser window to big
time.sleep(3)


# scrolling


scrollcount = 10
while scrollcount > 0:
    driver.find_element(By.TAG_NAME, 'body').send_keys((Keys.PAGE_DOWN))
    time.sleep(1)
    scrollcount -= 1

result = driver.find_elements(By.ID,  'dismissible')

t_list = []
c_list = []
for temp in result:
    title = temp.find_element(By.ID,'video-title').get_attribute('title')  # inside the html of video-title <div id='video-title'='유추브'>
    ccount = temp.find_element(By.CLASS_NAME, 'inline-metadata-item') # views

    print(title)
    print(ccount.text)
    t_list.append(title)
    c_list.append(ccount)

result_dict = {}
result_dict['title'] = t_list
result_dict['count'] = c_list

df = pd.DataFrame.from_dict(result_dict)
df.to_csv('연세대학교.csv')
print('-------------------------')



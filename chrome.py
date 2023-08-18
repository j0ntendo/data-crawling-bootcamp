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
url = "https://search.shopping.naver.com/search/all?query=%EC%98%88%EA%B2%AC%EC%9A%A9%ED%92%88&cat_id=&frm=NVSHATC"

# opening the chrome window
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True) # prevents the website from crashing
driver = webdriver.Chrome(options=chrome_options) # install chrome drive manager
driver.get(url)
driver.maximize_window()  # open the browser window to big
time.sleep(3)

# for scrolling down the webpage!!!!!
page_count = 15
while page_count > 0:
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    page_count -= 1



# now change pages with the button
pages = driver.find_elements(By.CLASS_NAME, 'pagination_btn_page___ry_S')  # the yellow part is the common class
print('pages :',len(pages))

t_list = []
p_list = []
d_list = []

for temp in range(0,2):
    pages[temp].click()
    time.sleep(2)

    page_count = 15
    while page_count > 0:
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        page_count -= 1

    titles = driver.find_elements(By.CLASS_NAME,'product_title__Mmw2K')  # these are found through chrome f12
    prices = driver.find_elements(By.CLASS_NAME,'product_price_area__eTg7I')
    short_menu = driver.find_elements(By.CLASS_NAME,'product_depth__I4SqY')

    for temp in range(len(titles)):
        print(titles[temp].text)
        print(prices[temp].text)
        print(short_menu[temp].text)

        t_list.append(titles[temp].text)
        p_list.append(prices[temp].text)
        d_list.append(short_menu[temp].text)
        print("--------------------------------------------")


result_dict = {}
result_dict['상품명'] = t_list
result_dict['가격'] = p_list
result_dict['분류'] = d_list

df = pd.DataFrame.from_dict(result_dict)
df.to_csv('애견용품.csv')


# {'상품명: [,,,,,,]

# x path uses
# //*[@id="container"]/div[1]/div/ul/li[1]/a
# //*[@id="container"]/div[1]/div/ul/li[2]/a
# for temp in range(5):
#     d = driver.find_element(By.XPATH, f'//*[@id="container"]/div[1]/div/ul/li[{temp+1}]/a')
#     print('연관검색어: ', d.text) # get rid of the text


# ------------------------------------------------------------------------------------------
# if other cases dont work then use this to get the html data from the website
# html = driver.page_source()
# print(html.text)
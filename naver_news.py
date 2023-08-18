import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import pandas as pd
import random


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()
url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=SK&oquery=%EC%9A%94%EA%B8%B0%EC%9A%94&tqi=iKLYhwp0YidssfnMjjGssssss8d-362915&nso=so%3Ar%2Cp%3Afrom20220728to20230728%2Ca%3Aall&de=2023.07.28&ds=2022.07.28&mynews=0&office_section_code=0&office_type=0&pd=3&photo=0&sort=0'

driver.get(url)
time.sleep(2)

titles_list = []
link_list = []
date_list = []
des_list = []

# while True:
for _ in range(40): # test
    titles = driver.find_elements(By.CLASS_NAME, 'news_tit')
    date = driver.find_elements(By.CLASS_NAME, 'info')
    des = driver.find_elements(By.CLASS_NAME, 'news_dsc')

    for temp in titles:
        titles_list.append(temp.get_attribute('title'))
        link_list.append(temp.get_attribute('href'))

    for temp in date:
        date_list.append(temp.text)

    for temp in des:
        des_list.append(temp.text)

    # print(len(titles), len(date), len(des))
    # print(titles_list)
    # print(link_list)
    # print(des_list)
    print(len(titles_list), len(link_list), len(des_list))


    try:
        page_index = driver.find_element(By.XPATH, '//*[@id="main_pack"]/div[2]/div/a[2]')
        page_index.click()
        time.sleep(random.randrange(2, 6))
    except:
        break

# print(page_index[0].get_attribute('aria-pressed'))
# for temp,temp1,temp2 in (titles,date,des):
#     print(temp.text)
#     print(temp1.text)
#     print(temp2.text)

# super last last
result_dict = {}
result_dict['titles'] = titles_list
result_dict['link'] = link_list
result_dict['des'] = des_list


pd.DataFrame.from_dict(result_dict).to_csv('test.csv', index=False, encoding='utf-8')


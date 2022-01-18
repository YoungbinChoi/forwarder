import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re

options = Options()
options.add_argument('headless')
options.add_argument('disable-logging')

cr_url = 'C:/Users/YB/PycharmProjects/Forwarding/chromedriver'
site_url = 'https://www.forwarder.kr/bbs/board.php?bo_table=space'

driver = webdriver.Chrome(cr_url, options = options)
driver.implicitly_wait(3)

url_list = []
#리스트 Url 로딩
for i in range(1,11):
    url = 'https://www.forwarder.kr/bbs/board.php?bo_table=space&page=' + str(i)
    driver.get(url)
    driver.implicitly_wait(0.5)
    for j in range(2,16):
        titles = driver.find_element_by_xpath(
            '// *[ @ id = "fboardlist"] / div[1] / table / tbody / tr[' + str(j) + '] / td[3] / a[2]')
        title = titles.get_attribute('href')
        url_list.append(title)
print(url_list)

def get_data(Url):
    response = driver.get(Url)
    html = driver.page_source
    soup7 = BeautifulSoup(html, 'html.parser')
    ex_id_divs = soup7.find('div', {'id' : 'view_contents'})
    return ex_id_divs

for i, url in enumerate(url_list):
    try:
        data = get_data(url)
        df = pd.DataFrame([{'story' : 'story_test_{}'.format(str(i)),
                            'episode' : 'episode_test_{}'.format(str(i))}])
    except:
        continue

    if i == 0:
        new_data = df.copy()
    else:
        new_data = pd.concat([new_data, df], axis=0)
print(new_data)











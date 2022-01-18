import time
import pandas as pd
import os
import pymysql
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import chromedriver_autoinstaller
import subprocess

driver = webdriver.Chrome('/chromedriver.exe')
driver.get('https://nid.naver.com/nidlogin.login?svctype=262144&url=http://m.naver.com/')

subprocess.Popen(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')
# ↑디버거 크롬 구동 컴퓨터 마다 크롬주소 확인 필요

option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
driver.implicitly_wait(10)
#driver.quit() #드라이버 종료

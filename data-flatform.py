from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

from datetime import datetime

import re

import requests

import time
import csv
import chromedriver_autoinstaller

import traceback

def is_element_present(driver, by, value):
    try:
        driver.find_element(by=by, value=value)
        return True
    except Exception:
        return False

def mid(k):
    return '#app > div.v-menu__content.theme--light.menuable__content__active > div > div > div:nth-child('+str(k)+') > a > div > div'


table=[]
tmid=[]

file=open('jst', 'r')

while True :
    line=file.readline()
    if len(line)==0:
        break
    line=line.lstrip()
    line=line.rstrip()
    temp=line.split()
    table.append(temp)
    tmid.append(int(temp[0].split('_')[0][1:]))

#int(table[0][0].split('_')[0][1:])

# selector 정의
table_manage='#style-1 > div.v-list.v-list--dense.v-list--subheader.theme--light > div:nth-child(4) > div > div'
drop_down='#app > div.application--wrap > main > div > div > div > nav > div > div:nth-child(3) > div > div.v-input__slot > div.v-select__slot > div.v-input__append-inner > div > i'
mid1='#app > div.v-menu__content.theme--light.menuable__content__active > div > div > div.primary--text > a > div > div'
mid2='#app > div.v-menu__content.theme--light.menuable__content__active > div > div > div:nth-child(2) > a > div > div'

load='#app > div.application--wrap > main > div > div > div > nav > div > button.mb-2.v-btn.theme--dark.purple'
create='#app > div.application--wrap > main > div > div > div > nav > div > button.mb-2.v-btn.theme--dark.primary
tag_inputbox='#app > div.application--wrap > main > div > div > div > nav > div > div:nth-child(7) > div > div.v-input__slot > div > input[type=text]'

##################### 크롤링 시작 #####################
url='http://dpdbtooltest.koscom.co.kr/'
driver = webdriver.Chrome()
driver.get(url)

time.sleep(1) #로그인 기다려줌
driver.find_element(By.CSS_SELECTOR, table_manage).click()
time.sleep(0.5) #페이지 이동 기다려줌

drop=driver.find_element(By.CSS_SELECTOR, drop_down)

inputbox=driver.find_element(By.CSS_SELECTOR,tag_inputbox)
inputbox.clear()                    #입력창 내용을 지우고
inputbox.send_keys('')              #입력창에 내용을 입력함


k=2
t=0
while True :
    try :
        drop.click()
        time.sleep(0.3) #dropdown 내려오는거 기다림
        target=driver.find_element(By.CSS_SELECTOR, mid(k))
        target_mid=int(target.text.split('/')[0])
        #mid   :   int(driver.find_element(By.CSS_SELECTOR, mid(k)).text.split('/')[0])


        k+=1
        

    except :
        break


'''
while True :
    print(driver.find_element(By.CSS_SELECTOR, mid(k)).text.split('/')[0])
    k+=1
'''

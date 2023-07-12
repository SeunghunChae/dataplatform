from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert       #alert 창 제어 모듈
from selenium.webdriver.chrome.options import Options   #headless
from bs4 import BeautifulSoup

from datetime import datetime

import re

import requests

import time
import csv
import chromedriver_autoinstaller

import traceback

#implicit wait이 안먹어서 while루프를 돌면서 태그가 뜰때까지 기다리게 만든 함수. exception을 회피하기 위해 만듦
#implicit wait : 태그가 생길때까지 기다려줌. time.sleep()보다 조금 더 좋으나 이상하게 작동 안할 때가 많음. 다음과 같이 사용한다.
#wait = WebDriverWait(driver, 10)
#table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, tab_name)))
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
table_manage='#style-1 > div.v-list.v-list--dense.v-list--subheader.theme--light > div:nth-child(5) > div.v-list__group__header > div:nth-child(2) > div > div > div'
drop_down='#app > div.application--wrap > main > div > div > div > nav > div > div:nth-child(3) > div > div.v-input__slot > div.v-select__slot > div.v-input__append-inner > div > i'
mid1='#app > div.v-menu__content.theme--light.menuable__content__active > div > div > div.primary--text > a > div > div'
mid2='#app > div.v-menu__content.theme--light.menuable__content__active > div > div > div:nth-child(2) > a > div > div'

tag_load='#app > div.application--wrap > main > div > div > div > nav > div > button.mb-2.v-btn.theme--dark.purple'
tag_create='#app > div.application--wrap > main > div > div > div > nav > div > button.mb-2.v-btn.theme--dark.primary'
tag_inputbox='#app > div.application--wrap > main > div > div > div > nav > div > div:nth-child(7) > div > div.v-input__slot > div > input[type=text]'

js_inputbox="document.querySelector(\"#app > div.application--wrap > main > div > div > div > nav > div > div:nth-child(7) > div > div.v-input__slot > div > input[type=text]\").value="

##################### 크롤링 시작 #####################
url='http://dpdbtooltest.koscom.co.kr/'

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')
driver = webdriver.Chrome(options=options) 
 
driver.get(url)

time.sleep(1) #로그인 기다려줌
driver.find_element(By.CSS_SELECTOR, table_manage).click()
time.sleep(1) #페이지 이동 기다려줌

drop=driver.find_element(By.CSS_SELECTOR, drop_down)

#투포인터 알고리즘
k=1 #드롭다운 iter
t=0 #mid list iter
while True :    
    try :
        drop.click()
        time.sleep(0.3) #dropdown 내려오는거 기다림
        target=driver.find_element(By.CSS_SELECTOR, mid(k))
        target_mid=int(target.text.split('/')[0])
        target.click()
        time.sleep(0.3)

        #버튼 드라이버 변수 설정
        inputbox=driver.find_element(By.CSS_SELECTOR,tag_inputbox)
        load=driver.find_element(By.CSS_SELECTOR,tag_load)
        create=driver.find_element(By.CSS_SELECTOR,tag_create)
               
        #드롭다운과 테이블명의 mid를 비교한 후 클릭을 수행한다.
        #table : 입력할 테이블명
        #tmid : 테이블 명 내의 mid
        #target_mid : 드롭다운 내의 mid
        while True:
            if tmid[t]==target_mid:
                #inputbox.clear()가 잘 안먹어서 자바스크립트로 강제로 입력
                driver.execute_script(js_inputbox+"''")
                driver.execute_script(js_inputbox+"'"+table[t][0]+"'")
                time.sleep(1)
                load.click()                        #로드버튼을 누르고
                time.sleep(1)
                create.click()                      #테이블생성 버튼을 누른다.
                time.sleep(1)

                t+=1
                print(table[t][0]+' 테이블 입력 성공하셨습니다. k: '+str(k)+'t : '+str(t)+'\n')

                #alert 창 닫기.
                window=Alert(driver)
                window.dismiss()
                time.sleep(0.5)
            else :
                break
            
        k+=1
        
    except :
        print('k : '+str(k)+'t : '+str(t)+'에서 에러남\n')
        break


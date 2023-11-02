# import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Selenium 4.6 버전부터는 옛날처럼 webdriver_manager import 할 필요 없다.
# from selenium import webdriver로 모든게 다 된다.
# driver = webdriver.Chrome() 코드의 Chrome() 부분 내부에도 추가로 코드를 작성할 필요 없어졌다.

# 아래는
# os.system('pip install --upgrade selenium')
# print(webdriver.__version__)

# 1. 세션 시작
driver = webdriver.Chrome()

# 2-1. 구글 검색창 검색어 입력 및 검색 실행
driver.get("https://google.com")
element = driver.find_element(By.NAME, 'q')
element.send_keys('맥도날드')
element.submit()

# 2-2. 네이버 검색창 검색어 입력 및 검색 실행
# driver.get("https://www.naver.com/")
# element = driver.find_element(By.ID, 'query')
# element.send_keys('맥도날드')
# element.submit()

time.sleep(10)

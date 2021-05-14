#뉴스 타이틀 크롤링
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')

driver = webdriver.Chrome('C:/Users/E_N__/Desktop/chromedriver.exe', chrome_options=options)
driver.get('https://sports.news.naver.com/kfootball/news/index.nhn?isphoto=N&type=popular')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('ul > li > div > a')

data = {}

for title in notices:
    data[title.text] = title.get('href')

print(data)

# with open(os.path.join(BASE_DIR, 'result.json'), 'w+', encoding='UTF-8-sig') as json_file:
#     json.dump(data, json_file, ensure_ascii=False)
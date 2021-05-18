#본문 예쁘게 크롤링
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
notices = soup.select('#_newsList > ul > li > div > a')

newslist = {}
content = {}
num = 1

for title in notices:
    url = title.get('href')
    if 'news' in url:
        url = 'https://sports.news.naver.com' + url
        newslist[title.text] = url
        driver.get(newslist[title.text])
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        notice = soup.select_one('#newsEndContents')

        output = ""
        for item in notice.contents:
            stripped = str(item).strip()
            if stripped == "":
                continue
            if stripped[0] not in ["<", "/"]:
                output += str(item).strip()
        output.replace("&apos;", "")
        content[url] = output

        with open(os.path.join(BASE_DIR + '/t05', 'news{}.txt'.format(num)),
                  'w+', encoding='UTF-8-sig') as text_file:
            text_file.write(content[url])
            num = num + 1
        # with open(os.path.join(BASE_DIR + '/t05', 'news{}.json'.format(num)), 'w+',
        #           encoding='UTF-8-sig') as json_file:
        #     json.dump(content, json_file, ensure_ascii=False)
        #     num = num + 1
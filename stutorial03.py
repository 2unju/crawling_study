#뉴스 타이틀 + 본문 크롤링
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

options = webdriver.ChromeOptions()
options.add_argument('headless')
#options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')

driver = webdriver.Chrome('C:/Users/E_N__/Desktop/chromedriver.exe', chrome_options=options)
driver.get('https://sports.news.naver.com/kfootball/news/index.nhn?isphoto=N&type=popular') #축구 전체
#driver.get('https://sports.news.naver.com/all/news/office.nhn?isphoto=N&ofc=076&type=popular') #스포츠조선
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('#_newsList > ul > li > div > a')
#_newsList > ul > li:nth-child(1) > div > a

news = {}
#newsEndContents > span:nth-child(1)
for title in notices:
    news[title.text] = title.get('href')

num = 0
context = dict()

for link in news:
    if '/read' not in news[link]:
        continue
    driver.get('https://sports.news.naver.com' + news[link])
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    #notice = soup.select('#newsEndContent')
    notice = soup.select_one('#newsEndContent')

    # if num == 5:
    #     print(notice)
    #
    # context[news[link]] = notice

    for para in notice:
        print(type(para))
        if news[link] in context:
            context[news[link]] += ('<br>' + str(para))
        else:
            context[news[link]] = str(para)

    with open(os.path.join(BASE_DIR + '/t03', 'news{}.json'.format(num)), 'w+',
              encoding='UTF-8-sig') as json_file:
        json.dump(context, json_file, ensure_ascii=False)
        num = num + 1

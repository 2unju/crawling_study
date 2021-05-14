from selenium import webdriver
from bs4 import BeautifulSoup
import json
import sys
import config
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cstudy.settings")
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "[project name].settings")
import django
django.setup()
from cDB.models import NewsData

#sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)) + '/app')))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def parse_news():
    driver = webdriver.Chrome('C:/Users/E_N__/Desktop/chromedriver.exe')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    notices = soup.select('ul > li > div > a')

    data = {}

    for title in notices:
        data[title.txt] = title.get('href')
    return data

if __name__ == '__main__':
    news_data_dict = parse_news()
    for t, l in news_data_dict.items():
        NewsData(title = t, link = l).save()

"""
## parser.py
import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websaver.settings")
import django
django.setup()
## BlogData를 import해옵니다
from parsed_data.models import BlogData

def parse_blog():
    req = requests.get('https://beomi.github.io/beomi.github.io_old/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select(
        'h3 > a'
        )
    data = {}
    for title in my_titles:
        data[title.text] = title.get('href')
    return data

## 이 명령어는 이 파일이 import가 아닌 python에서 직접 실행할 경우에만 아래 코드가 동작하도록 합니다.
if __name__=='__main__':
    blog_data_dict = parse_blog()
    for t, l in blog_data_dict.items():
        BlogData(title=t, link=l).save()
"""
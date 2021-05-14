#selenium.webdriver.find_by_element
# -> <selenium.webdriver.remote.webelement.WebElement(session = '', element = '')>
from selenium import webdriver
from bs4 import BeautifulSoup
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')

driver = webdriver.Chrome('C:/Users/E_N__/Desktop/chromedriver.exe', chrome_options=options)
driver.get('https://sports.news.naver.com/news.nhn?oid=076&aid=0003729295')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

print(soup.select('#newsEndContents'))
# print(type(soup.select_one('#newsEndContents')))
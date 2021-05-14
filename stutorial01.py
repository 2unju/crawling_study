#로그인
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:/Users/E_N__/Desktop/chromedriver.exe')
driver.get('https://sports.news.naver.com/kfootball/news/index.nhn?isphoto=N&type=popular')

#driver.find_element_by_name('user_id').send_keys('sione0025')
#driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/form/input[6]').send_keys('dpdlfls00')
#driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/form/button').click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('ul > li > div > a')

for n in notices:
    print(n.text.strip())
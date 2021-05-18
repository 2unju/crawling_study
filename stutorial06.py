#형태소 분석
import os
import json
#from konlpy.tag import Okt
from ckonlpy.tag import Twitter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file = open(os.path.join(BASE_DIR + '/t05/news1.txt'), 'r', encoding = 'UTF8')
text = file.read()
file.close()

#okt = Okt()
twitter = Twitter()
twitter.add_dictionary('K리그', 'Noun')

content = twitter.morphs(text)

num = 1
voca_dict = dict()
for word in content:
    voca_dict[num] = word
    num = num + 1

with open(os.path.join(BASE_DIR + '/t06', 'vocab.json'), 'w+',
          encoding='UTF-8-sig') as json_file:
    json.dump(voca_dict, json_file, ensure_ascii=False)
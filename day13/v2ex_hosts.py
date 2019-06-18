#-*- coding:utf-8 -*-
"""
Description
Date:2019/6/18 14:43
"""
import requests
from bs4 import BeautifulSoup


url = 'https://www.v2ex.com'
soup = BeautifulSoup(requests.get(url).text, 'html.parser')

for span in soup.find_all('span', class_= 'item_hot_topic_title'):
    print(span.find('a').text, span.find('a')['href'])
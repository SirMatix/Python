# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:32:37 2019

@author: Person1
"""

import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.nytimes.com/')
content = page.content
soup = BeautifulSoup(content, 'html.parser')
all_tags = soup.find_all('h2')
#print(list(i for i in all_tags))
list_of_headers = []
for i in all_tags:
    content = i.string
    list_of_headers.append(content)
for idx, i in enumerate(list_of_headers[:-2]):
    print(str(idx+1) + ' ' + i)
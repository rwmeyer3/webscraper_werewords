'''
Created on Jul 29, 2020

@author: rwmeyer3
'''
import requests
from bs4 import BeautifulSoup as BSoup
url = 'https://www.talkenglish.com/vocabulary/top-1500-nouns.aspx'
#url = 'https://www.ranker.com/crowdranked-list/the-most-influential-people-of-all-time'


response = requests.get(url)

soup = BSoup(response.text, 'lxml')
# f = open('xml.txt','w')
# f.write(response.text)
# f.close()
tags = soup.find_all('td', width='120')
#print(tags)
nouns = [tag.text.strip() for tag in tags]
nouns = nouns[1:]
#print(nouns)
#print(len(nouns))

f = open('nouns.txt','w')
for noun in nouns:
    f.write(noun+'\n')
f.close()

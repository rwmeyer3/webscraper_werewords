'''
Created on Jul 29, 2020

@author: rwmeyer3
'''
import requests
import string
from bs4 import BeautifulSoup as BSoup
#url = 'https://www.talkenglish.com/vocabulary/top-1500-nouns.aspx'
url = 'https://www.biographyonline.net/people/100-most-influential.html'


response = requests.get(url)

soup = BSoup(response.text, 'lxml')


#f = open('xml.txt','w')
#f.write(''.join(x for x in response.text if x in string.printable))
#f.close()
tags = soup.find_all('li')
#print(tags)
names = [tag.text.strip() for tag in tags]
names = names[20:-32]

for i in range(len(names)):
    if (names[i].find("US Pres")) > -1:
        names[i] = names[i][:names[i].find("US Pres")]
    if (names[i].find("Greek")) > -1:
        names[i] = names[i][:names[i].find("Greek")]
    if (names[i].find("(")) > -1:
        names[i] = names[i][:names[i].find("(")]
    if (names[i].find("c.")) > -1:
        names[i] = names[i][:names[i].find("c.")]
    names[i] = names[i].strip()
        

#print(names)
#print(len(names))

f = open('names.txt','w')
for name in names:
    f.write(name+'\n')
f.close()

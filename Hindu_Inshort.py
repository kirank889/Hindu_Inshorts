# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.thehindu.com/todays-paper/').text

soup = BeautifulSoup(source,'lxml')

#print(soup)

section = soup.find('div', class_='tpaper-container')

for category in section.find_all('a'):
    
    if category.text == 'sport' or category.text == 'business' or category.text == 'Front Page' :
        
        link = category['href']
        category_source = requests.get(link).text
        category_soup = BeautifulSoup(category_source,'lxml')
    
        print(category.text + ' headlines:\n' )
        #print(link)
        
        headlines = category_soup.find('div', class_='section-container')
        for lines in headlines.find_all('a'):
            try:
                print(lines.text)
        
            except Exception as e :
                #print(e)
                print('****error loading data****moving to next feed..')
			
        print()
           
    
    
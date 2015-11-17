# -*- coding: utf-8 -*-
import requests, mechanize, codecs
from pymongo import MongoClient
from bs4 import BeautifulSoup
#############################################
# client = MongoClient('localhost', 27017) #connext to mongodb
# db = client.questionDB	#create a database
# question = db.question #create a collection
#############################################
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0')]
#############################################
# br.open("http://www.nisshinkyo.org/search/terms.php")
# br.select_form(nr=1)
# response = br.submit(name='search')
# soup = BeautifulSoup(response, 'lxml')
# links = soup.find('table', {'class': 'termsDetail'}).find_all('a')
# for link in links:
# 	url = "http://www.nisshinkyo.org/search/"+link['href']
# 	name = link.text.strip()
# 	_line = name+url
# 	codecs.open("name.txt", 'a', 'utf-8').write(_line+"\n")

response = br.open("http://www.nisshinkyo.org/search/area.php?lng=1")
soup = BeautifulSoup(response, 'lxml')
areas = soup.find('div', {'id':'areajapan'}).find_all('a')
for i in xrange(len(areas)):
	prefecture = areas[i].text.strip()
	codecs.open("prefecture.txt", 'a', 'utf-8').write(prefecture+'\n')
#print soup.prettify()
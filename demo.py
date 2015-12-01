#!/usr/bin/python

import urllib2
from bs4 import BeautifulSoup
#print "Hello World!"

response = urllib2.urlopen('http://news.yahoo.co.jp/list/?d=20151127&c=economy&mc=f&mp=f')
html = response.read()
soup = BeautifulSoup(html,"html.parser")

returnList = []

for s in soup.find('ul', class_="list").find_all('li'):
    print s.find("span","ttl").string
    print s.find("span","cate").string
    print s.find("span","date").string
    print s.find('a', href=True)['href']
    if len(s.findAll('img')):
       print s.findAll('img')[0]['data-src']
    else:
       print "null"













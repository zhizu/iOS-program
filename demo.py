#!/usr/bin/python

import urllib2
import json,httplib
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
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('POST', '/1/classes/YahooNews', json.dumps({
       "title": s.find("span","ttl").string,
       "type": s.find("span","cate").string,
       "url": s.find('a', href=True)['href'],
       "newsdate": s.find("span","date").string
     }), {
       "X-Parse-Application-Id": "Pz7iwzIf7ocSS356iONXA8kiIxrUa9rteGIDbOp5",
       "X-Parse-REST-API-Key": "7aEJ3ogfoClcuFVU2Td66i6HWG5aC7ie9T4y2RpG",
       "Content-Type": "application/json"
     })
    results = json.loads(connection.getresponse().read())
    print results














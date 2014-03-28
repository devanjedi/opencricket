#!/usr/bin/python

from bs4 import BeautifulSoup
import re
import urllib3
import time
import pandas
#httpool = urllib3.PoolManager()
#response = httpool.request('GET','http://stats.espncricinfo.com/ci/engine/stats/index.html?class=1;opposition=8;team=2;template=results;type=bowling;view=innings')
#html = response.data


soup = BeautifulSoup(open("../../testdata/score.html"))

#print (soup.prettify())
t = soup.title.contents[0]
#print t.contents[0]
reg="([^:]*): (.*?) v (.*?) at ([^,]*), ([^|]*)| "
lt = re.compile(reg)
mo = lt.match(t)
test= mo.group(1)
team1 = mo.group(2)
team2 = mo.group(3)
location = mo.group(4)
date = mo.group(5)

print team1
print date

#for player in soup.find_all('a', class_="playerName"):
#    print player.string
#    print player.get('href')


#for i in range(1,11):
#    soup = BeautifulSoup(html)
#    time.sleep(1)
#    link= soup.find('a', class_="PaginationLink").get('href')
#    print link
#    response = httpool.request('GET','http://stats.espncricinfo.com'+link)
#    html = response.data
    
soup = BeautifulSoup(open('../../testdata/guru.html'))
tdata=soup.find(class_='guruNav').contents[0]
print tdata
#dfs = pandas.io.html.read_html(tdata)
#print dfs

#!/usr/bin/python

from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(open("score.html"))

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

for player in soup.find_all('a', class_="playerName"):
    print player.string
    print player.get('href')

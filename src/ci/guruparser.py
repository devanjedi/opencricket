#!/usr/bin/python

#Write a Stats Guru page to CSV

from bs4 import BeautifulSoup
import pandas
    
soup = BeautifulSoup(open('../../testdata/guru.html'))
tdata= soup.find_all(class_='engineTable')[2]

#print repr(tdata)
#dfs = pandas.read_html(repr(tdata))
#print dfs

dfs=pandas.read_html('http://stats.espncricinfo.com/ci/engine/stats/index.html?class=1;opposition=8;team=2;template=results;type=bowling;view=innings', attrs={'class':'engineTable'})
print dfs[2]
#dfs.to_csv('../../testdata/guru.csv')

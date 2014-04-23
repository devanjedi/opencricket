#!/usr/bin/python

#Write a Stats Guru page to CSV
#Will pull all pages, may be buggy
#Change url= to be the statsguru url to page 1
#Change f= to filename of resulting CSV
import pandas
    
url="http://stats.espncricinfo.com/ci/engine/stats/index.html?class=1;opposition=8;team=2;template=results;type=bowling;view=innings;"
pageNum=1
nextPage=1
f=open('../../testdata/guru.csv', 'a')
guruFrame = pandas.DataFrame()
while(nextPage):
    dfs=pandas.read_html(url+';page='+str(pageNum), attrs={'class':'engineTable'})[2]
    guruFrame=guruFrame.append(dfs)
    if len(dfs.index)<50:
        nextPage=0
    else:
        nextPage=1
    pageNum=pageNum+1
guruFrame.to_csv(f)

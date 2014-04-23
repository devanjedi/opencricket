#!/usr/bin/python

#Write a Stats Guru page to CSV
#Will pull all pages, may be buggy
#Change url= to be the statsguru url to page 1
#Change f= to filename of resulting CSV
import pandas
    
url="http://stats.espncricinfo.com/ci/engine/stats/index.html?class=1;opposition=3;team=6;template=results;type=bowling"
pageNum=1
nextPage=1
f=open('../../testdata/guru.csv', 'a')
guruFrame = pandas.DataFrame()
while(nextPage):
    dfs=pandas.read_html(url+';page='+str(pageNum), attrs={'class':'engineTable'},infer_types=False)[2]
    guruFrame=guruFrame.append(dfs)
    if len(dfs.index)<50:
        nextPage=0
    else:
        nextPage=1
    print "page %d done..." % pageNum
    pageNum=pageNum+1
print guruFrame
guruFrame.to_csv(f)

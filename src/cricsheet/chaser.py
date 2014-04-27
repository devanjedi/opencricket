#!/usr/bin/python

import yaml, os
dirtocheck="cricsheetIPL"
chaser=0
notchaser=0
for root, _, files in os.walk(dirtocheck):
    for f in files:
        with open(root+"/"+f) as doc:
            data=yaml.load(doc)
            if 'by' in data['info']['outcome']:
                matchoutcome= data['info']['outcome']['by']
                if 'wickets' in matchoutcome:
                    chaser=chaser+1
                elif 'runs' in matchoutcome:
                    notchaser=notchaser+1

print "chaser: %d" % chaser
print "notchaser: %d" % notchaser

#!/usr/bin/python
#This script will check all the cricsheet yaml files in directory
#specified by variable 'dirtocheck'.
#It will count how many matches were won by toss-winning team, and how
# many were won by side losing the toss and print results.

import yaml, os
dirtocheck="cricsheetT20I"
toss=0
nottoss=0
for root, _, files in os.walk(dirtocheck):
    for f in files:
        with open(root+"/"+f) as doc:
            data=yaml.load(doc)
            matchoutcome= data['info']['outcome']
            tossoutcome= data['info']['toss']
            if 'winner' in matchoutcome:
                if matchoutcome['winner'] == tossoutcome['winner']:
                    toss=toss+1
                else:
                    nottoss=nottoss+1
print "toss: %d" % toss
print "nottoss: %d" % nottoss

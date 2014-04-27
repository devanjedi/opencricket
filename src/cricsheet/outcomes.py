#!/usr/bin/python

import yaml, os
dirtocheck="cricsheetIPL"
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

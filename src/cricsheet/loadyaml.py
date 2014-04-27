#!/usr/bin/python

import yaml, os
dirtocheck="cricsheetIPL"
for root, _, files in os.walk(dirtocheck):
    for f in files:
        with open(root+"/"+f) as doc:
            data=yaml.load(doc)
            if data['info']['outcome']['winner'] == data['info']['toss']['winner']:
                print "yes"
            else:
                print "no"

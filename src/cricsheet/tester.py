#!/usr/bin/python

#Cricsheet helper tester

import cricsheet as cs
import yaml

with open("cricsheetIPL/335983.yaml") as doc:
	data=yaml.load(doc)
	cs.runsBetween(data,1,6)

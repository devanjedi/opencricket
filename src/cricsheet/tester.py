#!/usr/bin/python

#Cricsheet helper tester

import cricsheet as cs
import yaml

with open("../../localdata/ipl/335983.yaml") as doc:
	data=yaml.load(doc)
	print cs.getTeams(data)

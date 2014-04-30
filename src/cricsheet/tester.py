#!/usr/bin/python

#Cricsheet helper tester

import cricsheet as cs
import yaml

with open("cricsheetIPL/335983.yaml") as doc:
	data=yaml.load(doc)
#	cs.runsInOver(data,7)
#	cs.wicketDeliveries(data)
#	print cs.runsOnFirstLast(data)
	print cs.totalRunsInOver(data,7)
	print cs.runsInOver(data,7)

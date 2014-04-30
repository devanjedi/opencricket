#!/usr/bin/python

#Cricsheet helper functions

def getTeams(yamldoc):
	return yamldoc['info']['teams']
	
def getMatchWinner(yamldoc):
	matchoutcome= yamldoc['info']['outcome']
	if 'winner' in matchoutcome:
		return matchoutcome['winner']
	elif 'eliminator' in matchoutcome:
		return matchoutcome['eliminator']
	else:
		return['None']

def getTossWinner(yamldoc):
	return yamldoc['info']['toss']['winner']
	
def getBatsmen(yamldoc):
	for delivery in  yamldoc['innings'][0]['1st innings']['deliveries']:
		for info in delivery:
			print info

def runsBetween(yamldoc, start, end):
	for delivery in yamldoc['innings'][0]['1st innings']['deliveries']:
		delkey=delivery.keys()[0]
		if delkey<end+0.1 and delkey>=start:
			print delivery[delkey]

def runsInOver(yamldoc, over):
	runsBetween(yamldoc, over-1,over)

#returns balls in overs notation (21 balls is 3.3 overs)
def ballsToOvers(balls):
	return balls/6 + float(balls%6)/10

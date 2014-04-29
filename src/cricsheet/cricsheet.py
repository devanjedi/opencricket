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
	print yamldoc['innings'][0]['1st innings']['deliveries'][start-1][float(start)/10]['runs']['total']
	print  yamldoc['innings'][0]['1st innings']['deliveries'][end-1][float(end)/10]['runs']['total']

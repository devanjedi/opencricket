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
	


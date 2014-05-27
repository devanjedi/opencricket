#!/usr/bin/python

#Cricsheet helper functions

#Returns names of teams
def getTeams(yamldoc):
	return yamldoc['info']['teams']

#Returns name of match-winning team	
def getMatchWinner(yamldoc):
	matchoutcome= yamldoc['info']['outcome']
	if 'winner' in matchoutcome:
		return matchoutcome['winner']
	elif 'eliminator' in matchoutcome:
		return matchoutcome['eliminator']
	else:
		return['None']

#Returns name of toss-winning team
def getTossWinner(yamldoc):
	return yamldoc['info']['toss']['winner']
	
def getBatsmen(yamldoc):
	for delivery in  yamldoc['innings'][0]['1st innings']['deliveries']:
		for info in delivery:
			print info

#Print runs scored between start delivery and end delivery
#Format of deliveries is e.g. 1.3 would be 3rd delivery of 2nd over
def runsBetween(yamldoc, start, end):
	result={}
	for delivery in yamldoc['innings'][0]['1st innings']['deliveries']:
		delkey=delivery.keys()[0]
		if delkey<end+0.1 and delkey>=start:
			result[delkey]=delivery[delkey]['runs']['batsman']
	return result

def getLastDelivery(yamldoc, inning,offset):
	if inning==1:
		inningName='1st innings'
	elif inning==2:
		inningName='2nd innings'
	if offset==0:
		offset=-1
	else:
		offset=0-offset
	return yamldoc['innings'][int(inning)-1][inningName]['deliveries'][offset].keys()[0]


#Print the deliveries when wickets fall
def wicketDeliveries(yamldoc):
	for delivery in yamldoc['innings'][0]['1st innings']['deliveries']:
		delkey=delivery.keys()[0]
		if 'wicket' in delivery[delkey]:
			print delivery[delkey]

#Print the runs scored in a particular over
def runsInOver(yamldoc, over):
	return runsBetween(yamldoc, over-1,over)

def totalRunsBetween(yamldoc,start,end):
	runsB=runsBetween(yamldoc,start,end)
	total=0
	result={}
	for delivery in runsB:
		total=total+runsB[delivery]
	return total

def totalRunsInOver(yamldoc,over):
	runsinover=runsInOver(yamldoc, over)
	total=0
	result={}
	for delivery in runsinover:
		total=total+runsinover[delivery]
	return total

#returns balls in overs notation (21 balls is 3.3 overs)
def ballsToOvers(balls):
	return balls/6 + float(balls%6)/10

def runsOnDelivery(yamldoc,delivery):
	runsBetween(yamldoc,delivery, delivery)


def runsOnFirstLast(yamldoc):
	result={}
	over=0
	oldover=0
	for delivery in yamldoc['innings'][0]['1st innings']['deliveries']:
		delkey=delivery.keys()[0]
		over=int(delkey)
		if oldover<over:
			result[oldkey]=olddelivery[oldkey]['runs']['batsman']
		#print delkey,over
		if str(delkey-over) == str(0.1):
			result[delkey]=delivery[delkey]['runs']['batsman']
		runs=delivery[delkey]['runs']['batsman']
		oldover=over
		oldkey=delkey
		olddelivery=delivery
	result[delkey]=delivery[delkey]['runs']['batsman']
	return result

	

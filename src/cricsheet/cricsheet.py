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
	for delivery in yamldoc['innings'][0]['1st innings']['deliveries']:
		delkey=delivery.keys()[0]
		if delkey<end+0.1 and delkey>=start:
			print str(delkey)+","+ str(delivery[delkey]['runs']['batsman'])

#Print the deliveries when wickets fall
def wicketDeliveries(yamldoc):
	for delivery in yamldoc['innings'][0]['1st innings']['deliveries']:
		delkey=delivery.keys()[0]
		if 'wicket' in delivery[delkey]:
			print delivery[delkey]

#Print the runs scored in a particular over
def runsInOver(yamldoc, over):
	runsBetween(yamldoc, over-1,over)

#returns balls in overs notation (21 balls is 3.3 overs)
def ballsToOvers(balls):
	return balls/6 + float(balls%6)/10

def runsOnDelivery(yamldoc,delivery):
	runsBetween(yamldoc,delivery, delivery)


def runsOnFirstLast(yamldoc):
	over=0
	oldover=0
	for delivery in yamldoc['innings'][0]['1st innings']['deliveries']:
		delkey=delivery.keys()[0]
		over=int(delkey)
		if oldover<over:
			print str(oldkey)+","+  str(olddelivery[oldkey]['runs']['batsman'])
		#print delkey,over
		if str(delkey-over) == str(0.1):
			print str(delkey)+","+ str(delivery[delkey]['runs']['batsman'])
		runs=delivery[delkey]['runs']['batsman']
		oldover=over
		oldkey=delkey
		olddelivery=delivery
	print str(delkey)+","+ str(delivery[delkey]['runs']['batsman'])

#!/usr/bin/python
import logging #Handy Bug Fix
logging.basicConfig() #Handy Bug Fix - see https://github.com/pavoni/pyloopenergy/issues/14
import pyloopenergy  #pyloopenergy
import os #Environment Variables
import urllib.request #Web request


print("Starting")
def elec_trace():
	thisusagepoint = le.electricity_useage
	print("New Reading ", str(thisusagepoint))
	webrequest = urllib.request.urlopen(str(os.environ['url']) + "?kwh=" + str(thisusagepoint))
	if (str(webrequest.read().decode("utf-8")) != 'DONE'):
		print("Error sending result")
	 
print("Starting monitoring")
le = pyloopenergy.LoopEnergy(str(os.environ['serial']), str(os.environ['secret']))
le.subscribe_elecricity(elec_trace) #Start listening for data

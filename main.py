#!/usr/bin/python
import logging #Handy Bug Fix
logging.basicConfig() #Handy Bug Fix - see https://github.com/pavoni/pyloopenergy/issues/14
import pyloopenergy  #pyloopenergy
import os #Environment Variables
import urllib.request #Web request
from raven import Client #Logging
ravenErrorClient = Client('https://45d5760c5f86474693af392908cd6915:5b846b53fa2544a8af6d58e095cc43e2@sentry.io/193950') #Setup error client


print("Starting")
def elec_trace():
	thisusagepoint = le.electricity_useage
	print("New Reading ", str(thisusagepoint))
	webrequest = urllib.request.urlopen(str(os.environ['url']) + "?kwh=" + str(thisusagepoint))
	if (str(webrequest.read().decode("utf-8")) != 'DONE'):
		ravenErrorClient.captureMessage("Error sending result to server " + str(thisusagepoint))

print("Starting monitoring")
le = pyloopenergy.LoopEnergy(str(os.environ['serial']), str(os.environ['secret']))
le.subscribe_elecricity(elec_trace) #Start listening for data

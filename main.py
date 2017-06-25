#!/usr/bin/python
import logging #Handy Bug Fix
logging.basicConfig() #Handy Bug Fix - see https://github.com/pavoni/pyloopenergy/issues/14
import pyloopenergy  #Git Pull 
import sys #For command line arguments
import os #Environment Variables
import urllib.request #Web request

def elec_trace():
    global conncursor,meterdbrecord,conn
    thisusagepoint = le.electricity_useage
    print("New Reading ", str(thisusagepoint))
    webrequest = urllib.request.urlopen(str(os.environ['url']) + "?kwh=" + str(thisusagepoint))
	if (webrequest.read() != "DONE"):
		print("Error sending result")
   
print("Starting monitoring")
le = pyloopenergy.LoopEnergy(str(os.environ['serial']), str(os.environ['secret']))
try:
    le.subscribe_elecricity(elec_trace) #Start listening for data
except:
    print("***************************RESTARTING SCRIPT DUE TO EXCEPTION IN ENERGY MONITORING*************************** \n*")
    os.execl(sys.executable, sys.executable, *sys.argv)

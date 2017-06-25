#!/usr/bin/python
import logging #Handy Bug Fix
logging.basicConfig() #Handy Bug Fix - see https://github.com/pavoni/pyloopenergy/issues/14
import pyloopenergy  #Git Pull 
import sys #For command line arguments
import os #Environment Variables
import urllib.request #Web request
from flask import Flask #WebServer

app = Flask(__name__) #This is to keep Heroku Happy
app.run(os.environ.get('PORT')) #This is to keep Heroku Happy


def elec_trace():
    global conncursor,meterdbrecord,conn
    thisusagepoint = le.electricity_useage
    print("New Reading ", str(thisusagepoint))
    webrequest = urllib.request.urlopen(str(os.environ['url']) + "?kwh=" + str(thisusagepoint))
    if (webrequest.read() != "DONE"):
        print("Error sending result")
   
print("Starting monitoring")
le = pyloopenergy.LoopEnergy(str(os.environ['serial']), str(os.environ['secret']))
le.subscribe_elecricity(elec_trace) #Start listening for data

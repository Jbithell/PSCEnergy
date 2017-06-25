#!/usr/bin/python
import logging #Handy Bug Fix
logging.basicConfig() #Handy Bug Fix - see https://github.com/pavoni/pyloopenergy/issues/14
import pyloopenergy  #pyloopenergy
import sys #For command line arguments
import os #Environment Variables
import urllib.request #Web request
from flask import Flask #WebServer

print("Starting")
app = Flask(__name__) #This is to keep Heroku Happy
app.run(os.environ.get('PORT')) #This is to keep Heroku Happy
print("WebServer online")

while True:
	print("Hi")
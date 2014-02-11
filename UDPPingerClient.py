#Project 1
#Creators: Jonathan Thornton, Matthew Creamer
#Created on: 2/9/2014
#Last Editted on: 2/10/2014
#Purporse is to create a UDP pinger which sends 10 pings to
#a certain server in order to check out the files. This is the
#client for my server.

#UDPPingerClient.py

from socket import *
import time
serverName = 'localhost'
serverPort = 12005
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = 'Ping'
counter = 10 			#total number of pings we send to the server
i = 0 					#this will be our counted pings.
leftover = counter - i
print 'Sending '+ `counter` + 'to server \n'
while i < counter:
	i+= 1
print '\n Ping attempt number'+`i`+'is currently in progress. \n'
print 'Number of pings left: ' + `leftover`
dt= time.clock()
clientSocket.sendto(message,(serverName,serverPort))
clientSocket.settimeout(1)
try:
	modifiedMessage,serverAddress = clientSocket.recvfrom(1024)
	dt2 = time.clock()
	et = dt - dt2;
	print modifiedMessage
	print 'Time elapsed'+`et`+ 'microseconds. \n'
except timeout:
	print 'Request timed out'
if i == 10:
	clientSocket.close()

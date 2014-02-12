#Project 1
#Creators: Jonathan Thornton, Matthew Creamer
#Created on: 2/9/2014
#Last Editted on: 2/10/2014
#Purporse is to create a UDP pinger which sends 10 pings to
#a certain server in order to check out the files. This is the
#client for my server.

#UDPPingerClient.py

from socket import *
from datetime import datetime
serverName = 'localhost'
#serverName = '10.250.13.27'    Lucas address to test
serverPort = 12005
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = 'Ping'
counter = 10                    #total number of pings we send to the server
i = 0                                   #this will be our counted pings.
leftover = counter - i
lowestping = 10000000000 #this will be our lowest ping 
highestping = 0 #this will be the max number
pingpercent = 0
averageping = 0
acceptedpings = 0
print 'Sending '+ `counter` + 'to server \n'
while i < counter:
        i+= 1
        print '\n Ping attempt number '+`i`+' is currently in progress. \n'
        print 'Number of pings left: ' + `leftover`
        start= datetime.now()
        leftover = counter - i
        clientSocket.sendto(message,(serverName,serverPort))
        clientSocket.settimeout(1)
        try:
                modifiedMessage,serverAddress = clientSocket.recvfrom(1024)
                final = datetime.now()
                totaltime = start - final;
                averageping = averageping + totaltime.microseconds
                acceptedpings = acceptedpings+1
                if(totaltime.microseconds < lowestping):
                        lowestping = totaltime.microseconds
                if(totaltime.microseconds > highestping):
                        highestping = totaltime.microseconds
                print modifiedMessage
                print 'Time elapsed ',totaltime.microseconds,' microseconds. \n'
        except timeout:
                print 'Request timed out'
if i == 10:
        finalaverage = (averageping/acceptedpings)
        print 'Highest ping time was: ', highestping,'\n'
        print 'Lowest ping time was: ', lowestping,'\n'
        print 'Average ping time was: ', finalaverage, '\n'
        pingpercent = 1- acceptedpings/float(i)
        pingpercent = pingpercent*100
        print 'Percent loss was: ',pingpercent,'% \n'
        clientSocket.close()

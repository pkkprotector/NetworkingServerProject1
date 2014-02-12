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
serverName = 'localhost'        #This the server we're calling
#serverName = '10.250.13.27'    Lucas address to test
serverPort = 12005              #port number
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = 'Ping'                
counter = 10                    #total number of pings we send to the server
i = 0                                   #this will be our counted pings.
leftover = counter - i          #this keep track of the remaining pings
lowestping = 10000000 #this will be our lowest ping 
highestping = 0 #this will be the max number
pingpercent = 0 #this is the total percent of ping lost
averageping = 0 #this is our average ping count
acceptedpings = 0 #accepted pings counter
print 'Sending '+ `counter` + 'to server \n'
while i < counter:
        i+= 1           #increment
        print '\n Ping attempt number '+`i`+' is currently in progress. \n'
        print 'Number of pings left: ' + `leftover`
        start= datetime.now()  #what time ping was sent
        leftover = counter - i #decrements ping numbers
        clientSocket.sendto(message,(serverName,serverPort))   #sends ping to server
        clientSocket.settimeout(1)                      #max time is 1 second to send ping
        try:
                modifiedMessage,serverAddress = clientSocket.recvfrom(1024)
                final = datetime.now()          #time when ping came back
                totaltime = start - final;      #time from start to finish
                averageping = averageping + totaltime.microseconds #addes up counter
                acceptedpings = acceptedpings+1         #increments ping
                if(totaltime.microseconds < lowestping):
                        lowestping = totaltime.microseconds   #lowest time to ping
                if(totaltime.microseconds > highestping):
                        highestping = totaltime.microseconds  #highest time to ping
                
                #This returns the ping plus the time it took to return back to client
                print modifiedMessage
                print 'Time elapsed ',totaltime.microseconds,' microseconds. \n'
        except timeout:
                print 'Request timed out'
#Once the value is ten pings
if i == 10:
        finalaverage = (averageping/acceptedpings)           #calculated value of average ping
        print 'Highest ping time was: ', highestping,'\n'       #return highest ping
        print 'Lowest ping time was: ', lowestping,'\n'         #return lowest ping
        print 'Average ping time was: ', finalaverage, '\n'     #return average
        pingpercent = 1- acceptedpings/float(i)                 #calculates ping percent
        pingpercent = pingpercent*100                   
        print 'Percent loss was: ',pingpercent,'% \n'   #returns percent loss     
        clientSocket.close()                    #closes our connection to server

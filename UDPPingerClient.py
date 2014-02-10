#Project 1
#Creators: Jonathan Thornton, Matthew Creamer
#Created on: 2/9/2014
#Last Editted on: 2/10/2014
#Purporse is to create a UDP pinger which sends 10 pings to
#a certain server in order to check out the files. This is the
#client for my server.

#UDPPingerClient.py

from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socet(socket.AF_INET, socket.SOCK_DGRAM)
#Here is where ping goes
#
#
clientSocket.close()

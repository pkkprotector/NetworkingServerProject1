#Project 1
#Creators: Jonathan Thornton, Matthew Creamer
#Created on: 2/8/2014
#Last Editted on: 2/9/2014
#Purporse is to create a UDP pinger which sends 10 pings to
#a certain server in order to check out the files.

#UDPPingerServer.py
#We will need the following module to generate randomizzed lost packets
#import random
from socket import *
#Create a UDP Socket
#Notice the use of SOCK_DGRAM for UDP pacets
serverSocket = socket(AF_INET,SOCK_DGRAM)
#Assign IP address and port number to socket
serverSocket.bind(('',12000))
while True:
    #Generate random number in the range of 0 to 10
    rand = random.randint(0,10)
    #Receive the client packet along with the adddress it is coming from
    message, address = serverSocket.recvfrom(1024)
    #Capitalize the message from the client
    message = message.upper()
    #If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 4:
        continue
    #Otherwise, the server responds
    serverSocket.sendto(message, address)
    

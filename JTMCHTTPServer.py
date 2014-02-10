#Project 1
#Creators: Jonathan Thornton, Matthew Creamer
#Created on: 2/8/2014
#Last Editted on: 2/8/2014
#Purporse is to create a web server that will send a file to a client
#which is connected to the server.
#Requirements from Assignment 1 would be:
# i) create a connection socket(TCP)
# ii) recieve HTTP request from client
# iii) parse request and figure out what file is needed
# iv) get requested file from server
# v) create a header for the requeted file
# vi) send response over TCP

#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a socket
serverPort = 12000
serverSocket.bind(('localhost',serverPort))
serverSocket.listen(1)                   #lets server catch client's call
while True:
    #Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept()        #acceptes connection to client
    try:
        message, clientAddress = serverSocket.recvfrom(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = 'Message has been sent'
        #
        #Send one HTTP header line into socket
        #
        #
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        message, clientAddress = serverSocket.recvfrom(1024)
        errormsg = message('Error-could not recieve the file')
        connectionSocket.send(errormsg)
        #Close client socket
        connectionSocket.close()
        

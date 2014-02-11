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
serverPort = 12010
serverSocket.bind(('localhost',serverPort))
serverSocket.listen(1)                   #lets server catch client's call
while True:
    #Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept()        #acceptes connection to client
    try:
        message, clientAddress = connectionSocket.recvfrom(1024)
        print message
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() #F is file name. This reads in file
        print outputdata
        connectionSocket.send('HTTP/1.1 200 OK'+'\r\n\r\n')
        
        from time import gmtime, strftime
        currenttime = strftime("%a,%d,%b,%Y,%H:%M:%S+0000",gmtime())
        connectionSocket.send(currenttime+'\r\n')
        connectionSocket.send('Content Length: ' + `len(outputdata)` +'\r\n\r\n')
        connectionSocket.send('Conten Type: text/html'+'\r\n\r\n')
        connectionSocket.send('')
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found'+'\r\n\r\n')
        #Close client socket
        connectionSocket.close()
serverSocket.close()
        

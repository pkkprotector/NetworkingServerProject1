#Project 1
#Creators: Jonathan Thornton, Matthew Creamer
#Created on: 2/8/2014
#Last Editted on: 2/13/2014
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
from time import gmtime, strftime
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a socket
serverPort = 12010          #Sets socket number
serverSocket.bind(('localhost',serverPort))     #Binds socket to port
serverSocket.listen(1)                   #lets server catch client's call
while True:
    #Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept()        #accepts connection to client
    

    try:
        message, clientAddress = connectionSocket.recvfrom(1024)
        #Test case to see why my client crashes over time
        #print "the message: " + message

        #The reason why I have these statements is because my server will crash
        #because the message size is empty. 
        if len(message)==0:
            #This goes back to the top of the loop because the machine is accepting a 0 length string
            continue

        filename = message.split()[1]


        #Added in the close command this takes the command close from the window and turns the server off
        if filename == '/close':
            connectionSocket.send('<html><body>Server will now close. Thank you</body></html>')
            connectionSocket.send('<br/>')
            connectionSocket.send('<html><img src="http://cdn-ak.f.st-hatena.com/images/fotolife/a/aobanozomi/20110624/20110624033135.jpg" width="640" height="360"></html>')
            connectionSocket.close()
            serverSocket.close()

        f = open(filename[1:])      #This opens the file
        outputdata = f.read() #f is file name. This reads in file

        #print outputdata   #Test case to check if the value is being printed out.

        #The next six lines denote the file header before the data is actually outputted.
        connectionSocket.send('HTTP/1.1 200 OK'+'\n')       #Denotes that this is HTTP and type
        currenttime = strftime("Content Date: %a,%d,%b,%Y,%H:%M:%S",gmtime()) #This is the time 
        connectionSocket.send(currenttime+'\n')     #returns time
        connectionSocket.send('Content Length: ' + `len(outputdata)` +'\n')     #Returns length
        connectionSocket.send('Content Type: text/html'+'\r\n\r\n')         #Returns Type for file
        connectionSocket.send('')               #Requires empty space in our header
        connectionSocket.send(outputdata)       #Outputs file data
        
        #I don't need this statement because the output is sent in preceding statement
        #Send the content of the requested file to the client
        # for i in range(0, len(outputdata)):
        #     connectionSocket.send(outputdata[i])
        connectionSocket.close()        #done using the socket.
    
    except IOError:
        #Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found \r\n\r\n')
        connectionSocket.send('<html><body>File not found </body></html>')
        connectionSocket.close()  #Close client socket    
serverSocket.close()            #Closes server when done with files
        

#!/usr/bin/python3


import socket
import random

# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an almost-infinite loop; the loop can be stopped with Ctrl+C)

try:
    while True:

        numRand = str(random.randrange(999999999))
        newUrl = "http://localhost:1234/" + numRand

        print ('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print ('Request received:')
        print (recvSocket.recv(2048))
        print ('Answering back...')
        recvSocket.send(bytes("HTTP/1.1 302 Found\r\n\r\n" +
                        "<html><head>" +
                        "<html><head><meta http-equiv='refresh' content='2; " +
                        "url=http://localhost:1234/" + numRand + "'></head>" +                
                        "<body><h1>Moving to: </h1>" +
                        "<p>" + newUrl + "</p>" +
                        "</body></html>" +
                        "\r\n","utf-8"))
        recvSocket.close()
except KeyboardInterrupt:
    print ("Closing binded socket")
    mySocket.close()
#import socket module
from socket import *

# create an IPv4 TCP socket
serverPort = 6789
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
serverSocket.bind(('', serverPort))

# Listen for connections from client
serverSocket.listen(1)
print('Server initialized to recieve TCP Handshake Requests')

while True:
    # Establish the connection
    print ("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        print(message)
        message_split = message.split()
        if len(message_split) <= 1:
            # Small connection from browser - ignore
            connectionSocket.close()
            continue
            
        filename = message_split[1]
        f = open(filename[1:], "rb")
        outputdata = f.read()
        
        # Send one HTTP header line into socket
        #Fill in start     
        connectionSocket.send(b"HTTP/1.1 200 OK")

        if (filename.endswith(".jpg")):
            print("JPG SENDING!")
            connectionSocket.send(b"\r\nContent-type: image/jpeg")
        elif (filename.endswith(".gif")):
            print("GIF SENDING!")
            connectionSocket.send(b"\r\nContent-type: image/gif")
            
        
        connectionSocket.send(b"\r\n\r\n")
        #Fill in end
        
        # Send the content of the requested file to the client
        #Fill in start     
        connectionSocket.send(outputdata)
        #Fill in end
        
        # Close client socket
        #Fill in start     
        connectionSocket.close()
        #Fill in end        
    except IOError:
        #handle the case if the file has been moved to a new location
        #Fill in start
        #Fill in end
        
        #handle the case for file not found
        #Fill in start
        #Fill in end
        
        # sample code for a response
        connectionSocket.send(b'HTTP/1.1 426 Upgrade Required\r\n\r\n')
        # connectionSocket.send(b'<html><head></head><body><h1>This service requires use of the HTTP/1.1 protocol</h1></body></html>')
        
        # Close client socket
        # connectionSocket.close()
    except KeyboardInterrupt:
        # User pressed Ctrl+C, exit gracefully
        break
        
# Close server connection
serverSocket.close()

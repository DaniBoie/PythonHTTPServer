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
        
        # Send HTTP header line into socket
        connectionSocket.send(b"HTTP/1.1 200 OK")

        if (filename.endswith(".jpg")):
            print("JPG SENDING!")
            connectionSocket.send(b"\r\nContent-type: image/jpeg")
        elif (filename.endswith(".gif")):
            print("GIF SENDING!")
            connectionSocket.send(b"\r\nContent-type: image/gif")

        connectionSocket.send(b"\r\n\r\n")
        
        # Send the content of the requested file to the client
        connectionSocket.send(outputdata)
        
        # Close client socket
        connectionSocket.close()

    except IOError as e:
        errorFile = e.filename
        
        
        if (errorFile == "lab0.html"):
            #handle the case if the file has been moved to a new location
            connectionSocket.send(b"HTTP/1.1 301 Moved Permanently\r\n\r\n")
            connectionSocket.send(b'<html><head></head><body><h1>lab0.html has been moved to lab2.html</h1></body></html>')
        else:
            #handle the case for file not found
            connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
            connectionSocket.send(b'<html><head></head><body><h1>File Requested not found</h1></body></html>')

        # connectionSocket.send(b'HTTP/1.1 426 Upgrade Required\r\n\r\n')
        # connectionSocket.send(b'<html><head></head><body><h1>This service requires use of the HTTP/1.1 protocol</h1></body></html>')
        
        # Close client socket
        connectionSocket.close()
    except KeyboardInterrupt:
        # User pressed Ctrl+C, exit gracefully
        break
        
# Close server connection
serverSocket.close()

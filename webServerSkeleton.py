#import socket module
from socket import *

# create an IPv4 TCP socket
#Fill in start     
#Fill in end

# Prepare a sever socket
#Fill in start     
#Fill in end

# Listen for connections from client
#Fill in start     
#Fill in end

while True:
    # Establish the connection
    print ("Ready to serve...")
    connectionSocket, addr = #Fill in start     #Fill in end
    try:
        message = #Fill in start     #Fill in end
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
        #Fill in end
        
        # Send the content of the requested file to the client
        #Fill in start     
        #Fill in end
        
        # Close client socket
        #Fill in start     
        #Fill in end        
    except IOError:
        #handle the case if the file has been moved to a new location
        #Fill in start
        #Fill in end
        
        #handle the case for file not found
        #Fill in start
        #Fill in end
        
        # sample code for a response
        # connectionSocket.send(b'HTTP/1.1 426 Upgrade Required\r\n\r\n')
        # connectionSocket.send(b'<html><head></head><body><h1>This service requires use of the HTTP/1.1 protocol</h1></body></html>')
        
        # Close client socket
        #Fill in start     
        #Fill in end
    except KeyboardInterrupt:
        # User pressed Ctrl+C, exit gracefully
        break
        
# Close server connection
serverSocket.close()

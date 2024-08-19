# Citation for the following code/format:
# Date: 10/18/2023
# Adapted from: "Computer Networking: A Top-Down Approach" by James Kurose and Keith Ross, 7th Edition
# Kurose&Ross Chapter 2.7.2

from socket import *

# Target server and port
serverName = "gaia.cs.umass.edu"
serverPort = 80

# Create the client socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect the client socket to the server
clientSocket.connect((serverName, serverPort))

# Define the HTTP request
request = "GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost: gaia.cs.umass.edu\r\n\r\n"
print ("Request: ", request) # added to match response example from assignment

# Send client request to the server
clientSocket.send(request.encode())

# Receive the response
response = clientSocket.recv(1024) #buffer size
print("[RECV] - length: ", len(response)) # added to match response example from assignment

# Print the response
print(response.decode())

# Close the socket
clientSocket.close()
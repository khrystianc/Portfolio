# Citation for the following code/format:
# Date: 10/18/2023
# Adapted from: "Computer Networking: A Top-Down Approach" by James Kurose and Keith Ross, 7th Edition
# Kurose&Ross Chapter 2.7 (TCPServer.py)

from socket import *

# Define the port number
serverPort = 8001

# Create a listening socket bound to '127.0.0.1' and port above
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)  # Listen for incoming connections

print(f"Connected by http://127.0.0.1:{serverPort}")

while True:
    # Accept a connection from a client
    connectionSocket, addr = serverSocket.accept()

    # Receive the client request
    request = connectionSocket.recv(1024).decode()

    # Print the client's request
    print(f"Received:\n{request}\n")

    # Send the response
    data =  "HTTP/1.1 200 OK\r\n"\
            "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
            "<html>Congratulations!  You've downloaded the first Wireshark lab file!</html>\r\n"

    connectionSocket.send(data.encode())

    # Close the connection socket
    connectionSocket.close()

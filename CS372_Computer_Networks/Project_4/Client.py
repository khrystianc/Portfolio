# Citation for the following code/format:
# Date: 12/06/2023
# Adapted from: "Computer Networking: A Top-Down Approach" by James Kurose and Keith Ross, 7th Edition
# logic adapted from SKT_GET.py and SKT_Bigger_GET.py assignment (project 1 of CS372)
# logic adapted from https://github.com/gcallant/Rock-Paper-Scissors-Multiclient-Server
# logic adapted from https://stackoverflow.com/questions/52687450/rock-paper-scissors-game-using-sockets-in-python

from socket import *
import logging # https://www.geeksforgeeks.org/logging-in-python/

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("client.log"),
                              logging.StreamHandler()])

# logic adapted from SKT_GET.py, SKT_Bigger_GET.py assignment (project 1 of CS372)
def client_program():
    # Set host and port for the client to connect to
    serverName = 'localhost'
    serverPort = 65432  # Should match the port used by the server

    try:
        # Create the client socket
        clientSocket = socket(AF_INET, SOCK_STREAM)
        # Create a TCP socket and connect it to the server
        clientSocket.connect((serverName, serverPort))
        logging.info("Connected to server.")
        print("Connected to the server. Type '/q' to quit.")
    except Exception as e:
        logging.error(f"Unable to connect to server: {e}")
        clientSocket.close()
        return

    # Main loop for continuous interaction with the server
    while True:
        # Prompt the user to enter a message
        message = input("Enter Input > ")
        # Send the message to the server
        clientSocket.sendall(message.encode())

        # Check if the message is a command to quit ('/q')
        if message.lower() == '/q':
            break

        try:
            # Receive a response from the server
            data = clientSocket.recv(4096)
            server_msg = data.decode()
            logging.info(f"Server: {server_msg}")

            # Break the loop if no data is received or if '/q' command is received
            if not data or server_msg == '/q':
                logging.info("No data received. Server may be closed.")
                break

            else:
                # Print the server's response
                print(f"Server: {server_msg}")

        except Exception as e:
            logging.error(f"Error receiving data: {e}")
            break

    clientSocket.close()
    logging.info("Connection closed.")

# Function to handle the Rock-Paper-Scissors game
# logic adapted from https://github.com/gcallant/Rock-Paper-Scissors-Multiclient-Server
# logic adapted from https://stackoverflow.com/questions/52687450/rock-paper-scissors-game-using-sockets-in-python
def play_rock_paper_scissors(s):
    # Game loop for playing Rock-Paper-Scissors
    while True:
        # Receive a message from the server
        data = s.recv(4096)
        server_msg = data.decode()

        # Check if the game has ended based on the server's message
        if "wins!" in server_msg or "It's a tie!" in server_msg:
            print(server_msg)
            break  # Exit the game loop if the game has ended

        # Print the server's message and wait for the client's move
        print(server_msg, end=' ')
        move = input()  # Get the client's move
        s.sendall(move.encode())  # Send the move to the server

# Entry point of the program
if __name__ == '__main__':
    client_program()

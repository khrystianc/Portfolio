# Citation for the following code/format:
# Date: 12/06/2023
# Adapted from: "Computer Networking: A Top-Down Approach" by James Kurose and Keith Ross, 7th Edition
# logic adapted from http_server.py assignment (project 1 of CS372)
# logic adapted from https://github.com/gcallant/Rock-Paper-Scissors-Multiclient-Server
# logic adapted from https://stackoverflow.com/questions/52687450/rock-paper-scissors-game-using-sockets-in-python

from socket import *
import random
import logging # https://www.geeksforgeeks.org/logging-in-python/

# Configure logger
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("server.log"),
                              logging.StreamHandler()])

# logic adapted from http_server.py assignment (project 1 of CS372)
def server_program():
    # Set host and port for the server
    serverHost = 'localhost'
    serverPort = 65432  # desired port number

    try:
        # Create a TCP socket and bind it to the host and port above
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind((serverHost, serverPort))
        serverSocket.listen()  # Listen for incoming connections
        logging.info("Server listening...")

        # Greet the user and provide instructions
        print("Server is running and ready to accept connections.")
        print("Type '/q' to shut down the server.")
        
        # Accept a connection from a client
        connectionSocket, addr = serverSocket.accept()
        with connectionSocket:
            print(f"Connected by {addr}")  # Print the address of the connected client

            # Main loop to continuously handle client messages
            while True:
                data = connectionSocket.recv(4096)  # Receive data from the client
                # Break the loop if no data is received or if '/q' command is received
                if not data or data.decode() == '/q':
                    print("Received '/q', shutting down the server...")
                    break

                print(f"Client: {data.decode()}")  # Print the client's message

                # Check if the received message is a command to play Rock-Paper-Scissors
                if data.decode().lower() == "play rock-paper-scissors":
                    # Play the game and print the result
                    result = play_rock_paper_scissors(connectionSocket)
                    print(result)
                    continue  # Continue to the next iteration of the loop

                # If not playing a game, prompt the server user for a reply
                reply = input("Enter Input > ")
                connectionSocket.sendall(reply.encode())  # Send the reply to the client
    
    except OSError as e:
        logging.error(f"Error binding to port {serverPort}: {e}")
        return
    
    finally:
        logging.info("Closing server socket.")
        serverSocket.close()

# Function to handle the Rock-Paper-Scissors game
# logic adapted from https://github.com/gcallant/Rock-Paper-Scissors-Multiclient-Server
# logic adapted from https://stackoverflow.com/questions/52687450/rock-paper-scissors-game-using-sockets-in-python
def play_rock_paper_scissors(conn):
    # Get the player's move from the client
    player_move = get_game_input(conn)
    # Randomly select the server's move
    server_move = random.choice(["rock", "paper", "scissors"])
    # Determine the winner of the game
    result = determine_winner(player_move, server_move)
    # Send the game result to the client
    conn.sendall(f"Server chose {server_move}. {result}".encode())
    return "Rock-Paper-Scissors game ended."

# Function to get the game move from the client
def get_game_input(conn):
    while True:
        # Ask the client for their move
        conn.sendall("Your move (rock, paper, scissors): ".encode())
        move = conn.recv(4096).decode().lower()  # Receive the move
        # Validate the move and return it if valid
        if move in ["rock", "paper", "scissors"]:
            return move
        else:
            # Inform the client if the move is invalid
            conn.sendall("Invalid move. Try again.".encode())

# Function to determine the winner of the Rock-Paper-Scissors game
def determine_winner(player_move, server_move):
    # Determine the winner based on the rules of Rock-Paper-Scissors
    if player_move == server_move:
        return "It's a tie!"
    elif (player_move == "rock" and server_move == "scissors") or \
         (player_move == "paper" and server_move == "rock") or \
         (player_move == "scissors" and server_move == "paper"):
        return "Player wins!"
    else:
        return "Server wins!"

# Entry point of the program
if __name__ == '__main__':
    server_program()

# Author: Khrystian Clark
# Date: 3/3/2020
# Description:  Creates a game of TicTacToe, meant to be played by two players.



"""Write a class named TicTacToe that has two private data members: the board, and the current state."""
class TicTacToe:
    """list of three lists that each contain three empty strings (where each represents an empty square)"""
    list_a = ["_", "_ ", "_"]
    list_b = ["_", "_", "_"]
    list_c = ["_", "_", "_"]
    board = (list_a,
             list_b,
             list_c)
    current_state = "UNFINISHED"
    """the board, which will be a list of lists that represent a 3x3 board"""
    def __init__ (self, board, current_state):
        self._board = board
        self._current_state = current_state

    def get_current_state(self): #have a get method named get_current_state
        return self._current_state

    def make_move(self, row, column, x_or_o):
        if el in list_a or list_b or list_c == "X" or "O":
            return False

        if ((row < 0) or (row > 2)) or ((column < 0) or (column > 2)):
            return False

        """Assigning value to x_or_o"""
        self._board[row][column] = x_or_o

        """If the game is already over or there are no more moves to be made"""
        if self._current_state == "X_WON" or "O_WON" or "DRAW":
            return False

        """Situations if player_x wins"""
        if list_a[0] == "X" and list_a[0] == list_b[0] and list_b[0] == list_c[0]:
            return self._current_state == "X_WON"
        if list_a[1] == "X" and list_a[1] == list_b[1] and list_b[1] == list_c[1]:
            return self._current_state == "X_WON"
        if list_a[2] == "X" and list_a[2] == list_b[2] and list_b[2] == list_c[2]:
            return self._current_state == "X_WON"
        if list_a[0] == "X" and list_a[0] == list_b[1] and list_b[1] == list_c[2]:
            return self._current_state == "X_WON"
        if list_a[2] == "X" and list_a[2] == list_b[1] and list_b[1] == list_c[0]:
            return self._current_state == "X_WON"
        if list_a[0] == "X" and list_a[0] == list_a[1] and list_a[1] == list_a[2]:
            return self._current_state == "X_WON"
        if list_b[0] == "X" and list_b[0] == list_b[1] and list_b[1] == list_b[2]:
            return self._current_state == "X_WON"
        if list_c[0] == "X" and list_c[0] == list_c[1] and list_c[1] == list_c[2]:
            return self._current_state == "X_WON"

        """Situations if player_o wins"""
        if list_a[0] == "O" and list_a[0] == list_b[0] and list_b[0] == list_c[0]:
            return self._current_state == "O_WON"
        if list_a[1] == "O" and list_a[1] == list_b[1] and list_b[1] == list_c[1]:
            return self._current_state == "O_WON"
        if list_a[2] == "O" and list_a[2] == list_b[2] and list_b[2] == list_c[2]:
            return self._current_state == "O_WON"
        if list_a[0] == "O" and list_a[0] == list_b[1] and list_b[1] == list_c[2]:
            return self._current_state == "O_WON"
        if list_a[2] == "O" and list_a[2] == list_b[1] and list_b[1] == list_c[0]:
            return self._current_state == "O_WON"
        if list_a[0] == "O" and list_a[0] == list_a[1] and list_a[1] == list_a[2]:
            return self._current_state == "O_WON"
        if list_b[0] == "O" and list_b[0] == list_b[1] and list_b[1] == list_b[2]:
            return self._current_state == "O_WON"
        if list_c[0] == "O" and list_c[0] == list_c[1] and list_c[1] == list_c[2]:
            return self._current_state == "O_WON"

        """If there are no more possible moves left or if the players are at a stalemate"""
        else:
            return "DRAW"


"""Luwey example"""
class TicTacToe:
    """ This class represents the Tic Tac Toe game """
    def __init__(self):
        """ Initializes the board and current state"""
        self._current_state = 'UNFINISHED'
        self._board = [['' for _ in range(3)] for _ in range(3)]
    def get_current_state(self):
        """ Gets the current state"""
        return self._current_state
    # printing board for debugging purposes
    def print_board(self):
        """ Prints the board out"""
        for row in self._board:
            print(row)
    def make_move(self, row, column, player):
        """ This functions makes the move for the Tic Tac Toe game"""
        # check to make sure game is not finished
        if self._current_state != 'UNFINISHED':
            return False
        # check to make sure valid index
        if not (0 <= row <= 2) or not (0 <= column <= 2):
            return False
        # check to make sure player is valid
        if player != 'x' and player != 'o':
            return False
        # check to make sure a spot isn't occupied
        if self._board[row][column] != '':
            return False
        # makes the move for the play
        self._board[row][column] = player
        # runs the check for winner function
        self.check_for_winner()
        return True
    def check_for_winner(self):
        """ This checks for the winning combinations """
        # check for row wins
        for row in self._board:
            if row[0] == row[1] == row[2] == 'x':
                self._current_state = 'X_WON'
                return
            if row[0] == row[1] == row[2] == 'o':
                self._current_state = 'O_WON'
                return
        # check columns wins
        for i in range(3):
            if self._board[0][i] == self._board[1][i] == self._board[2][i] == 'x':
                self._current_state = 'X_WON'
                return
            if self._board[0][i] == self._board[1][i] == self._board[2][i] == 'o':
                self._current_state = 'O_WON'
                return
        # check for diagonal win going top left to bottom right
        if self._board[0][0] == self._board[1][1] == self._board[2][2] == 'x':
            self._current_state = 'X_WON'
            return
        if self._board[0][0] == self._board[1][1] == self._board[2][2] == 'o':
            self._current_state = 'O_WON'
            return
        # checks for diagonal win going top right to bottom left
        if self._board[0][2] == self._board[1][1] == self._board[2][0] == 'x':
            self._current_state = 'X_WON'
            return
        if self._board[0][2] == self._board[1][1] == self._board[2][0] == 'o':
            self._current_state = 'O_WON'
            return
        # check for draw
        for row in self._board:
            for i in range(3):
                if row[i] == '':
                    return
        self._current_state = 'DRAW'
# The code below is for debugging purposes
if __name__ == '__main__':
    ttt = TicTacToe()
    # ttt.check_for_winner()
    while 1:
        row = int(input('Row input:'))
        col = int(input('Col input:'))
        player = input('Player:')
        ttt.make_move(row, col, player)
        ttt.print_board()
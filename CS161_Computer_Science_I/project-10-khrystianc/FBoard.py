# Author: Khrystian Clark
# Date: 3/11/2020
# Description:  This program creates a strategy game between two players, kind of like war mixed with chess. Enjoy!

class FBoard:
    """establishes the class given as FBoard with elements below"""

    def __init__(self):
        """This step initializes the board and the starting game state for the users"""
        self._board = [["_", "_", "_", "_", "_", "_", "_", "_"],
                       ["_", "_", "_", "_", "_", "_", "_", "_"],
                       ["_", "_", "_", "_", "_", "_", "_", "_"],
                       ["_", "_", "_", "_", "_", "_", "_", "_"],
                       ["_", "_", "_", "_", "_", "_", "_", "_"],
                       ["_", "_", "_", "_", "_", "_", "_", "o"],
                       ["_", "_", "_", "_", "_", "_", "o", "_"],
                       ["_", "_", "_", "_", "_", "o", "_", "o"]]
        self._game_state = "UNFINISHED"
        player_x = "x"
        self._board[0][0] = player_x

    def get_game_state(self):
        """Returns the current state of the game."""
        return self._game_state

    """ Prints the board out"""
    def print_board(self):
        for line in self._board:
            print(line)

    """Establish the criteria for a player to make a move"""
    def establish_move(self, row, column, player):
        # check to make sure game is not finished
        if self._game_state != 'UNFINISHED':
            return False
        # check to make sure valid index
        if not (0 <= row <= 7) or not (0 <= column <= 7):
            return False
        # check to make sure player is valid
        if player != 'x' and player != 'o':
            return False
        # check to make sure a spot isn't occupied
        if self._board[row][column] != '_':
            return False
        # makes the move for the play
        self._board[row][column] = player
        return True

    """Player "x" moves"""
    def move_x(self, row, column):
        if self._board[row][column] != (row + 1 or - 1) and self._board[row][column] != (column + 1 or - 1):
            return False
        if self._board[row][column] == "x" or "o":
            return False
        else:
            self._board[row][column] = player_x
            #leaves the previous "x" on the board, not in criteria to take that away
        """For x as a winner"""
        if self._board[7][7] == player_x:
            self._game_state = "X_WON"
            return self._game_state


    """player "o" moves"""
    def move_o(self, row, column, end_row, end_column):
        if self._board[row][column] != "o":
            return False
        if self._board[row][column] == "o":
            self._board[row][column] = "_"
            self._board[end_row][end_column] = "o"
            return self._game_state
        """Establishes if "o" is making a valid diagonal move"""
        if end_row != (row + 1 or - 1) and end_column != (column + 1 or - 1):
                return False
        """Establish criteria for "o" winning"""
        if "x" == self._board[6][7] or self._board[7][6]:
            self._game_state = "O_WON"
            return self._game_state
        else:
            return False

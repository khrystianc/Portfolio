# Author: Khrystian Clark
# Date: 11/24/2020
# Description: Final portfolio project: A FocusGame program that has two players playing the Focus Game.
#               program validates moves, returns reserve and captured statuses, and returns the winner.

class FocusGame:
    """Class for the abstract focus game"""

    def __init__(self, _player1, _player2):
        """Initialize the game board with a list of lists. Initialized the players ad private data members
        and initialized two holding lists for the reserved and captured pieces"""
        list_a = ['R', 'R', 'G', 'G', 'R', 'R']
        list_b = ['G', 'G', 'R', 'R', 'G', 'G']
        list_c = ['R', 'R', 'G', 'G', 'R', 'R']
        list_d = ['G', 'G', 'R', 'R', 'G', 'G']
        list_e = ['R', 'R', 'G', 'G', 'R', 'R']
        list_f = ['G', 'G', 'R', 'R', 'G', 'G']
        self._board = (list_a,
                       list_b,
                       list_c,
                       list_d,
                       list_e,
                       list_f)
        self._player1 = _player1
        self._player2 = _player2
        self._reserved = []  # empty lists to store the reserve and captured pieces
        self._captured = []
        self._move_count1 = 0  # Count the users moves to track turns
        self._move_count2 = 0

    def move_piece(self, _player, _start_loc, _end_loc, _num_pieces):
        """Method that validates the players move, and makes the move. Then calls another method to update the
        the reserve and captured lists of pieces, then calls another method to check for a winner based on
        the list of pieces captured. Otherwise returns an error message if the move is invalid (11 lines)"""
        start_x = _start_loc[0]
        start_y = _start_loc[1]
        end_x = _end_loc[0]
        end_y = _end_loc[1]
        if self.take_turns(_player) is True:
            if self.validate_move(_player, _start_loc, _end_loc, _num_pieces) is True:
                self._board[end_x][end_y] = self._board[start_x][start_y][0:_num_pieces] + self._board[end_x][end_y]
                self._board[start_x][start_y] = self._board[start_x][start_y][_num_pieces:]
                self.sideline_update(self._board[end_x][end_y][5:], _player)
                self._board[end_x][end_y] = self._board[end_x][end_y][0:5]
                return self.check_winner()
            else:
                return self.validate_move(_player, _start_loc, _end_loc, _num_pieces)
        else:
            return self.take_turns(_player)

    def take_turns(self, _user):
        """Makes players take turns, assuming that player 1 will always go first. If it is that player's turns
        it increases their move count by one. Then uses the move counts to find whose turn it is.(13 lines)"""
        if _user == self._player1[0]:
            if self._move_count1 > self._move_count2:
                return "not your turn"
            else:
                self._move_count1 += 1
                return True
        if _user == self._player2[0]:
            if self._move_count1 <= self._move_count2:
                return "not your turn"
            else:
                self._move_count2 += 1
                return True
        return False

    def validate_move(self, _player, _start, _end, _pieces):
        """Validates the move, and returns the error messages, otherwise returns true, the make_move method finishes
        (19 lines)"""
        start_x = _start[0]
        start_y = _start[1]
        end_x = _end[0]
        end_y = _end[1]
        if (start_x or end_x or start_y or end_y) < 0:
            return "invalid location"
        if (start_x or end_x or start_y or end_y) > 5:
            return "invalid location"
        if len(self._board[start_x][start_y]) < _pieces:
            return "invalid number of pieces"
        if (((start_x - end_x) ** 2) + ((start_y - end_y) ** 2)) > _pieces ** 2:
            return "invalid number of pieces"
        if self._player1[0] == _player:
            if self._player1[1] != self._board[start_x][start_y][0]:
                return "not your turn"
        if self._player2[0] == _player:
            if self._player2[1] != self._board[start_x][start_y][0]:
                return "not your turn"
        return True

    def show_pieces(self, _board_loc):
        """takes a position on the board and returns a list showing the pieces that are present at that location with
        the bottom-most pieces at the 0th index of the array and other pieces on it in the order. (4 lines)"""
        x_coord = _board_loc[0]
        y_coord = _board_loc[1]
        location = self._board[x_coord][y_coord]
        return [i for i in location][::-1]  # reverse the list to put bottom pieces at 0th location

    def show_reserve(self, _player):
        """takes the player name as the parameter and shows the count of pieces that are in reserve for the player.
        If no pieces are in reserve, return 0. (6 lines)"""
        if _player == self._player1[0]:
            return self._reserved.count(self._player1[1])
        if _player == self._player2[0]:
            return self._reserved.count(self._player2[1])
        else:
            return 0

    def show_captured(self, _player):
        """takes the player name as the parameter and shows the number of pieces captured by that player.
        If no pieces have been captured, return 0. (6 lines)"""
        if _player == self._player1[0]:
            return self._captured.count(self._player2[1])
        if _player == self._player2[0]:
            return self._captured.count(self._player1[1])
        else:
            return 0

    def reserved_move(self, _player, _board_loc):
        """Takes the player name and the location on the board as the parameters. It places the piece from the reserve
         to the location. It should reduce the reserve pieces of that player by one and make appropriate adjustments to
         pieces at the location. If there are no pieces in reserve, return 'no pieces in reserve'.
         Communicates with reserve string, and init method to place pieces on the board. (20 lines)"""
        x_coord = _board_loc[0]
        y_coord = _board_loc[1]
        if self.take_turns(_player) is True:
            if _player == self._player1[0]:
                if self._reserved.count(self._player1[1]) > 0:
                    self._reserved.remove(self._player1[1])
                    self._board[x_coord][y_coord] = self._player1[1] + self._board[x_coord][y_coord]
                    return "reserve move successful"
                else:
                    return "no pieces in reserve"
            if _player == self._player2[0]:
                if self._reserved.count(self._player2[1]) > 0:
                    self._reserved.remove(self._player2[1])
                    self._board[x_coord][y_coord] = self._player2[1] + self._board[x_coord][y_coord]
                    return "reserve move successful"
                else:
                    return "no pieces in reserve"
            return "no pieces in reserve"
        else:
            return self.take_turns(_player)

    def sideline_update(self, _excess, _player):
        """Takes two variables from the method that calls this method and uses them to update the list of reserve
        and the list of captured pieces, directly after a successful move is made. (10 lines)"""
        extra = [i for i in _excess]
        for a in extra:
            if _player == self._player1[0]:
                if a == self._player1[1]:
                    self._reserved.append(a)
                self._captured.append(a)
            else:
                if a == self._player2[1]:
                    self._reserved.append(a)
                self._captured.append(a)

    def check_winner(self):
        """Method called after the update of the lists to find if there is a winner, based on the captured pieces
        list. If not, it returns successful move. (5 lines)"""
        if self._captured.count(self._player1[1]) >= 6:
            return self._player2[0] + " Wins"
        if self._captured.count(self._player2[1]) >= 6:
            return self._player1[0] + " Wins"
        return "successfully moved"

# Author: Khrystian Clark
# Date: 2/5/2020
# Description:  Gives the odometer distance that a taxi has travelled between points.

class Taxicab:
    """A class to keep track of taxi location and odometer reading.
    :attributes:
        _x_coord : int
            a private data member to store left/right coordinate values
        _y_coord : int
            a private data member to store down/up coordinate values
        _odometer : int
            a private data member to store units moved
    :methods:
        move_x : helper func
            modifies _x_coord
            modifies _odometer
        move_y : helper func
            modifies _y_coord
            modifies _odometer
    :getters:
        get_x_coord : int
            get the x position
        get_y_coord : int
            get the y position
        get_odometer : int
            get the odometer reading
    """
    # private class attributes
    def __init__(self, x_coord, y_coord):
        """Insantiate private data members for the Taxicab class."""
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._odometer = 0
    # move the taxi left or right
    def move_x(self, units):
        """Move the Taxicab left or right."""
        self._odometer += abs(units)
        self._x_coord += units
    # move the taxi down or up
    def move_y(self, units):
        """Move the Taxicab down or up."""
        self._odometer += abs(units)
        self._y_coord += units
    # get the x-coordinate
    def get_x_coord(self):
        """Getter for the x position."""
        return self._x_coord
    # get the y-coordinate
    def get_y_coord(self):
        """Getter for the y position."""
        return self._y_coord
    # get the odometer reading
    def get_odometer(self):
        """Getter for the odometer reading."""
        return self._odometer
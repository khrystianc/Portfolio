# Author: Khrystian Clark
# Date: 10/20/2020
# Description: a program that takes the height width and length and returns the volume of the box measurements.

class Box:
    """Class that hold takes in the measurements of the box"""
    def __init__(self, _length, _width, _height):
        """Initializes the variables that hold the measurements as private data members"""
        self._length = _length
        self._width = _width
        self._height = _height

    def get_length(self):
        """Get method for length"""
        return self._length

    def get_width(self):
        """Get method for width"""
        return self._width

    def get_height(self):
        """Get method for height"""
        return self._height

    def volume(self):
        """Calculates the volume of the box"""
        return self._length * self._width * self._height


def box_sort(boxes):
    """insertion sort that sorts a list of boxes from greatest volume to smallest."""
    for box in range(1, len(boxes)):
        value = boxes[box]
        pos = box - 1
        while pos >= 0 and value.volume() > boxes[pos].volume():
            boxes[pos + 1] = boxes[pos]
            pos -= 1
        boxes[pos + 1] = value

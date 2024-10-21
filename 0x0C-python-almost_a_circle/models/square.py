#!/usr/bin/python3
"""This module defines the Square class which inherits from the
Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines a square and it's methods"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes an isinstance of the Square class

        Args:
            size (int): size of the square
            x (int): x coordinate of the square
            y (int): y coordinate of the square
            id (int): id of the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string rep of the square"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
                self.width)

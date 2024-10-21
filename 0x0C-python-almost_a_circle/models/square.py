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

    @property
    def size(self):
        """Gets the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the square using args or kwargs"""
        if args:
            attr = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attr):
                    setattr(self, attr[i], arg)

        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the square"""
        return {
                "id": self.size,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """Returns the string rep of the square"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
                self.width)

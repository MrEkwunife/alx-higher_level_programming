#!/usr/bin/python3


"""define a `rectangle` class"""


class Rectangle:
    """rectangle class"""
    def __init__(self, width=0, height=0):
        """initialize arguments
        Args:
            width (int)
            height (int)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width property after validating"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height property after validating"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

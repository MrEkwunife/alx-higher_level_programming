#!/usr/bin/python3

"""This module is all about creating a Square"""


class Square:
    """this is Square class to create a blueprint for square shape."""

    def __init__(self, size=0):
        """this special method initialize data.
        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """this returns the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """this sets the size to value.
        Args:
            value (int): the value to set to size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """this method returns the square of size"""
        return (self.__size ** 2)

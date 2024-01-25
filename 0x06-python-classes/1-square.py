#!/usr/bin/python3

"""This module is all about creating a Square"""


class Square:
    """this is Square class to create a blueprint for square shape."""

    def __init__(self, size):
        """this special method initialize data.
        Args:
            size (int): The size of the square.
        """
        self.__size = size

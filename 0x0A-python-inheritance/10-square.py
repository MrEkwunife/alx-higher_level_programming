#!/usr/bin/python3

"""Square class inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle"""

    def __init__(self, size):
        """constructor method: initialize"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area implemented"""
        return (self.__size * self.__size)

    def __str__(self):
        """return string represetation of the class"""
        return f"[Rectangle] {self.__size}/{self.__size}"

#!/usr/bin/python3

"""Rectangle class inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """constructor method: initialize"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area implemented"""
        return (self.__width * self.__height)

    def __str__(self):
        """return string represetation of the class"""
        return f"[Rectangle] {self.__width}/{self.__height}"

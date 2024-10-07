#!/usr/bin/python3
"""A rectangle Class Module"""


class Rectangle:
    """Defines the blueprint for creating rect objects"""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): width of the new rectangle
            height (int): height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calcs and returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returnd the printable representation of the rectangle.

        Represents the rect with # char
        """
        if self.__width == 0 or self.height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append('\n')

        return "".join(rect)

    def __repr__(self):
        """ Return the string representation of the rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        """Prints a message for the deletion of a rectangle"""
        print("Bye rectangle...")

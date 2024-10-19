#!/usr/bin/python3
# File: rectangle.py
# Author: Chimobi E.
"""This Module contains the implementation of the Rectangle

It inherits from the Base Class
"""
from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Intializes the Rectangle class

        Args:
            self: object itself
            width (int): width of the new rectangle
            height (int): height of the new rectangle
            x (int): x coordinate of the rectangle
            y (int): y coordinate of the rectangle
            id (int): identity of the new rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')

        if value <= 0:
            raise ValueError('width must be > 0')

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
        if value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @property
    def x(self):
        """Gets the x coordinate of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x coordinate of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @property
    def y(self):
        """Gets the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y coordinate of the rectangle"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')

        self.__y = value

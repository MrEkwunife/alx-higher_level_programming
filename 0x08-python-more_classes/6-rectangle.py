#!/usr/bin/python3


"""define a `rectangle` class"""


class Rectangle:
    """rectangle class
    Args:
        number_of_instances (int)
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialize arguments
        Args:
            width (int)
            height (int)
        """
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

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

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """informal string representation of the rectangle object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = ""
        for i in range(self.__height):
            for _ in range(self.__width):
                rect += "#"
            rect += "\n"
        return rect[:-1]

    def __repr__(self):
        """formal string representation of the rectangle object"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """delete object"""
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")

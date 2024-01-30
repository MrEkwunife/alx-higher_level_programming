#!/usr/bin/python3


"""define a `rectangle` class"""


class Rectangle:
    """rectangle class
    Args:
        number_of_instances (int)
        print_symbol (any)
    """
    number_of_instances = 0
    print_symbol = "#"

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
                # rect += "#"
                rect += str(self.print_symbol)
            rect += "\n"
        return rect[:-1]

    def __repr__(self):
        """formal string representation of the rectangle object"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """delete object"""
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method to compare the size of two Rectangles
        Args:
            rect_1 (Rectangle)
            rect_2 (Rectangle)
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() == rect_2.area()) or (rect_1.area() > rect_2.area()):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """class method to create a square rectangle(size,size)
        Args:
            cls: class Rectangle
            size: int
        """
        return cls(size, size)

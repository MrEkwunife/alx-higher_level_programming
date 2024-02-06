#!/usr/bin/python3

""" BaseGeometry class"""


class BaseGeometry:
    """this is an empty class"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
            Args:
                name: str
                value: int
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

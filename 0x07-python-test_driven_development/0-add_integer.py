#!/usr/bin/python3

"""This module is about TDD - Test Driven Development
functions:
    add_integer
"""


def add_integer(a, b=98):
    """ function adds two integers.
    Args:
        a (int): first int.
        b (int): 2nd int (defaults to 98).
    """
    if not a or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))

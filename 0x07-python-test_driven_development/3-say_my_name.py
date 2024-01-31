#!/usr/bin/python3

"""this module house the function `say_my_name`"""


def say_my_name(first_name, last_name=""):
    """function prints first and lst name
    Args:
        first_name (str): first name
        last_name (str): last name
    Raises:
        TypeError: first name and last name must be string
    """

    if first_name:
        if type(first_name) is not str:
            raise TypeError("first_name must be a string")
        if type(last_name) is not str:
            raise TypeError("last_name must be a string")
        print(f"My name is {first_name} {last_name}")
    else:
        raise TypeError("first name must be given")

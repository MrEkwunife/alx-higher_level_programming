#!/usr/bin/python3
"""
Module Contains the base class of future classess or objects

More Docs...
"""
import json


class Base:
    """The Base class of which other Classes would be inheriting from inorder
    to avoid code duplication

    Attributes:
        __nb_objects (int): Number of instatiated Bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Intialize a new Base

        Args:
            id (int): The identity of the new base
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a json string of a dict"""
        return "[]" if not list_dictionaries else json.dumps(list_dictionaries)

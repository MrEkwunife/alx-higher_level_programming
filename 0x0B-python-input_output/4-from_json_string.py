#!/usr/bin/python3
"""Modules contains a function that returns a python obj from json"""
import json


def from_json_string(my_str):
    """Returns python object"""
    return json.loads(my_str)

#!/usr/bin/python3
"""Contains a function that returns the JSON(string) rep of an obj"""
import json


def to_json_string(my_obj):
    """Return JSON rep of an object"""
    return json.dumps(my_obj)

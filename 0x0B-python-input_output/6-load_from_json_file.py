#!/usr/bin/python3
"""Contains a function that returns an object from JSON"""
import json


def load_from_json_file(filename):
    """Returns an object from a json"""
    with open(filename) as f:
        return json.load(f)

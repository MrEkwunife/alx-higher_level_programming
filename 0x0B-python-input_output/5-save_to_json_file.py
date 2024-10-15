#!/usr/bin/python3
"""Contains a function that writes into a json file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a file using Json representation"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)

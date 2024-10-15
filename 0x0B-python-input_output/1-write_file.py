#!/usr/bin/python3
"""Contains a function that writes to a file"""


def write_file(filename="", text=""):
    """Writes in utf-8 into a file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

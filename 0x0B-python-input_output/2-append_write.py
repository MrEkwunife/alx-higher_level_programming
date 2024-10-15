#!/usr/bin/python3
"""Contains a function that appends some texts to a file"""


def append_write(filename="", text=""):
    """Appends text to filename contents"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)

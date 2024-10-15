#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')

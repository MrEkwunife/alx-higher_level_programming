#!/usr/bin/python3
"""Module contains IO functions"""


def class_to_json(obj):
    """Returns dict rep of a simple data structure"""
    return obj.__dict__

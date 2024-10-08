#!/usr/bin/python3
"""Locked Class Implementation"""


class LockedClass:
    """Attributes must be called 'firstname' else error"""

    __slots__ = ["first_name"]

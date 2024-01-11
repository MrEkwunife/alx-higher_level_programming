#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new = {}
    for key, val in a_dictionary.items():
        new[key] = val * 2
    return new

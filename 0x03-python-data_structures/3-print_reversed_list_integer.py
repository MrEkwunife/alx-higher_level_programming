#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        for m in my_list[::-1]:
            print("{:d}".format(m))

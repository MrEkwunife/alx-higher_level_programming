#!/usr/bin/python3

'''
def print_reversed_list_integer(my_list=[]):
    start = -1
    end = len(my_list) * -1

    while end <= start:
        print("{:d}".format(my_list[start]))
        start -= 1
'''


def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))

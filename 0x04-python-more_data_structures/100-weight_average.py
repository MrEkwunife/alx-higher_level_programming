#!/usr/bin/python3

def weight_average(my_list=[]):
    if not isinstance(my_list, list) or not my_list:
        return 0

    avg = 0
    size = 0
    for i, k in my_list:
        avg += i * k
        size += k
    return avg / size

#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if not (idx < 0 or idx > len(my_list) - 1):
        new_list[idx] = element

    return (new_list)

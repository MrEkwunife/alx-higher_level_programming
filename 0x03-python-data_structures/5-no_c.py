#!/usr/bin/python3


def no_c(my_string):
    new_list = [i for i in my_string if i not in ["c", "C"]]
    return "".join(new_list)

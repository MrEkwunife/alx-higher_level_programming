#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)

    max_ = my_list[0]
    for list_ in my_list:
        if list_ > max_:
            max_ = list_
    return (max_)

#!/usr/bin/python3


def search_replace(my_list, search, replace):
    newlist = []
    for i in my_list:
        if i == search:
            newlist.append(replace)
        else:
            newlist.append(i)
    return newlist

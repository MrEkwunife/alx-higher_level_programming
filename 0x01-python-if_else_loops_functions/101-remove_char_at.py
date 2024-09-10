#!/usr/bin/python3
def remove_char_at(str, n):
    lst = list(str)
    if 0 <= n < len(str):
        lst.pop(n)
    return ("".join(lst))

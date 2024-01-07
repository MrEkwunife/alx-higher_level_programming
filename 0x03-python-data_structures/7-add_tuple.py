#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        a_1 = 0
        a_2 = 0
    elif len(tuple_a) == 1:
        a_1 = tuple_a[0]
        a_2 = 0
    else:
        a_1 = tuple_a[0]
        a_2 = tuple_a[1]

    if len(tuple_b) == 0:
        b_1 = 0
        b_2 = 0
    elif len(tuple_b) == 1:
        b_1 = tuple_a[0]
        b_2 = 0
    else:
        b_1 = tuple_b[0]
        b_2 = tuple_b[1]

    c_1 = a_1 + b_1
    c_2 = a_2 + b_2
    c = (c_1, c_2)

    return c

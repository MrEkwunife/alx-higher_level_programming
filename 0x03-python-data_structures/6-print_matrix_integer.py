#!/usr/bin/python3
'''
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and len(matrix[0]) == 0:
        return
    for row in matrix:
        for i in range(len(row) - 1):
            col = row[i]
            print("{:d} ".format(col), end="")
        print(row[-1], end="")
        print()
'''


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print("{:d}".format(col), end=" " if col != row[-1] else "")
        print()

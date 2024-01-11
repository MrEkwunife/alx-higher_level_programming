#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    newMatrix = []

    for i in matrix:
        temp = []
        for j in i:
            temp.append(j ** 2)
        newMatrix.append(temp)
    return newMatrix

#!/usr/bin/python3


# print a matrix
def print_matrix_integer(matrix=[[]]):
    [print("{:d}".format(m), end="") for mat in matrix for m in mat]



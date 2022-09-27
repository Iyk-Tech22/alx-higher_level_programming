#!/usr/bin/python3


# print a matrix
def print_matrix_integer(matrix=[[]]):
    for matrice in matrix:
        print(" ".join("{:d}".format(item) for item in matrice))

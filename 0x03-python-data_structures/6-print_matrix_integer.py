#!/usr/bin/python3


# print a matrix
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for matrice in matrix:
            for vec in matrice:
                print("{:d}".format(vec), end=" ")
            print("")



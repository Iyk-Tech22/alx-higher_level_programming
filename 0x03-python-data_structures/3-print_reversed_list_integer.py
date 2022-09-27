#!/usr/bin/python3


# Revearse a list
def print_reversed_list_integer(my_list=[]):
    [print("{:d}".format(item)) for item in my_list[::-1]]

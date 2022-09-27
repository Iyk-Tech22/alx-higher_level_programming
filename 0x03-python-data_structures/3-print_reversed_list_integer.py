#!/usr/bin/python3


# Revearse a list
def print_reversed_list_integer(my_list=[]):
    new_list = my_list[::-1]
    [print("{:d}".format(item)) for item in new_list]

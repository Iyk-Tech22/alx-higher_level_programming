#!/usr/bin/python3


# Revearse a list
def print_reversed_list_integer(my_list=[]):
    list_size = len(my_list) - 1
    reverse_list = [my_list[list_size - index]\
                    for index, item in enumerate(my_list)]
    [print("{:d}".format(item)) for item in reverse_list]

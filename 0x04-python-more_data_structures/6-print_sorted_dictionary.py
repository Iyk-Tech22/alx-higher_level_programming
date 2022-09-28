#!/usr/bin/python3


# Print dictionary in a sorted order
def print_sorted_dictionary(a_dictionary):
    dic = sorted(a_dictionary.items())
    for key, value in dic:
        print("{:s}: {}".format(key, value))

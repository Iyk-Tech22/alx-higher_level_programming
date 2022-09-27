#!/usr/bin/python3


# Remove all cases of c charater from a string
def no_c(string):
    new_string = ""
    for char in string:
        if char != "c" and char != "C":
            new_string += char
    return new_string

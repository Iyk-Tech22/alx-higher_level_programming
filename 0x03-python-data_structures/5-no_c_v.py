#!/usr/bin/python3


# Remove all cases of c charater from a string
def c_checking(char):
    return (char != "c" and char != "C")
def no_c(string):
    new_string = [char for char in string if c_checking(char)]
    return (str(new_string))

#!/usr/bin/python3


# Delete a key from a dictionary
def simple_delete(a_dictionary, key=""):
    if key and key in a_dictionary:
        del a_dictionary[key]
        return (a_dictionary)
    else:
        return (a_dictionary)

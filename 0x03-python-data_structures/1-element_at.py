#!/usr/bin/python3


# fetch an element by it index from a list
def element_at(my_list, idx):
    if idx < 0:
        return (None)
    elif idx > len(my_list) - 1:
        return (None)
    else:
        return (my_list[idx])

#!/usr/bin/python3


# Replace a specific elem in a list without changing the original list
def new_in_list(my_list, idx, elem):
    if idx < 0:
        return (my_list)
    elif idx > len(my_list) - 1:
        return (my_list)
    else:
        new_list = [item for item in my_list]
        new_list[idx] = elem
        return (new_list)

#!/usr/bin/python3


# Replace a element at specified index in list
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)
    elif idx > len(my_list) - 1:
        return (my_list)
    else:
        my_list[idx] = element

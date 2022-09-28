#!/usr/bin/python3


# Sum all unique values in a list
def uniq_add(my_list=[]):
    unique_list = []
    sum_unique = 0
    if len(my_list) == 0:
        return (0)
    for item in my_list:
        unique = True
        for val in unique_list:
            if item == val:
                unique = False
                break
        if unique:
            unique_list.append(item)
            sum_unique += item
    return (sum_unique)

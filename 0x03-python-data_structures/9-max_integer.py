#!/usr/bin/python
def max_integer(my_list=[]):
    if not my_list:
        return (None)
    else:
        max = 0
        for i in my_list:
            if max < i:
                max = i
        return (max)

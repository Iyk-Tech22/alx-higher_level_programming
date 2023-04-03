#!/usr/bin/python3
""" Find a peak in a list of unsorted integers """

def peak_finder(int_list):
    """Find a peak in list of integers"""

    if int_list == None or into_list == []:
        return None
    lower = 0
    high = len(int_list)
    middle = ((high - lower // 2) + lower
    middle = int(middle)
    if high == 1:
        return int_list[0]
    if high == 2:
        return max(int_list)
    if int_list[middle] >= int_list[middle - 1] and\
            int_list[middle] >= int_list[middle + 1]:
        return int_list[middle]
    if middle > 0 and int_list[middle] < int_list[middle + 1]:
        return peak_finder(int_list[middle:])
    if middle > 0 and int_list[middle] < int_list[middle - 1]:
        return peak_finder(int_list[:middle])

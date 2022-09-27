#!/usr/bin/python3
get_element_at = __import__("1-element_at").element_at

list_items = [20,12,47,90]
idx = int(input("Enter Item Index Here: "))
elem = get_element_at(list_items,idx)
print("element at index {:d} is {}".format(idx, elem))

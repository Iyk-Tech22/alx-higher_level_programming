#!/usr/bin/python3
new_in_list = __import__("4-new_in_list").new_in_list
my_list = [2,4,5,7]
idx = 3
elem = 6
new_list = new_in_list(my_list, idx, elem)
print(my_list)
print(new_list)

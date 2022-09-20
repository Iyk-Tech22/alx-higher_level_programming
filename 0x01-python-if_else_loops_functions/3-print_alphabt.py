#!/usr/bin/python3
x = 97
while x <= 122:
    if x != ord('q') and x != ord('e'):
        print("{}".format(chr(x)), end="")
    x += 1

#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    argc = len(args)
    text = "{:d} arguement".format(argc)
    if argc == 0:
        text += "s."
    elif argc == 1:
        text += ":"
    elif argc >= 2:
        text += "s:"
    print(text)
    for i, arg in enumerate(args):
        print("{:d}: {:s}".format(i+1, arg))

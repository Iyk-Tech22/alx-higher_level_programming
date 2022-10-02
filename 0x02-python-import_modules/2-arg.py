#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    argc = len(args)
    text = "{:d} arguement".format(argc)
    if argc == 0:
        text += "s."
    elif argc == 1:
        text += "s:"
    args = " "
    if len(sys.argv) == 1:
        print("{:d} arguments.".format(0))
    elif len(sys.argv) == 2:
        args = sys.argv[1]
        print("{:d} argument:".format(1))
        print("{:d}: {:s}".format(1, args))
    else:
        text += "s:"
    print(text)
    for i, arg in enumerate(args):
        print("{:d}: {:s}".format(i, arg))

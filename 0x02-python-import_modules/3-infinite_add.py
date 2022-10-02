#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":  
    args = argv
    args.pop(0)
    sum = 0 
    for arg in args:
        sum += int(arg)
print("{:d}".format(sum))

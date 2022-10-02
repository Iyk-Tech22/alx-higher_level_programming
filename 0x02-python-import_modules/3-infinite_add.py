#!/usr/bin/python3
from sys import argv

if __name__ == "__main__": 
    argv.pop()   
    args = argv
    sum = 0 
    for arg in args:
        sum += int(arg)
print("{:d}".format(sum))

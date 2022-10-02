#!/usr/bin/python3
from  sys import argv

if __name__ == "__main__":    
    sum = 0
    args = argv.pop()
    for arg in args:
        sum += int(arg)
print("{:d}".format(sum))

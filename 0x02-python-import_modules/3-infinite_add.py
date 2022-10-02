#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":  
    args = argv
    args.pop(0)
    print(sum(map(int, args)))

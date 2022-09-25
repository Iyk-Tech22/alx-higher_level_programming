#!/usr/bin/python3


if __name__ == "__main__":
    from  sys import argv    
    sum = 0
    args = argv[1:]
    for arg in args:
        sum += int(arg)
print("{:d}".format(sum))

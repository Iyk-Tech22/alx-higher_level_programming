#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = " "
    if len(sys.argv) == 1:
        print("{:d} arguments.".format(0))
    elif len(sys.argv) == 2:
        args = sys.argv[1]
        print("{:d} argument:".format(1))
        print("{:d}: {:s}".format(1, args))
    else:
        args = sys.argv[1:]
        print("{:d} arguments:".format(len(args)))
        for i, arg in enumerate(args):
            print("{:d}: {:s}".format(i, arg))
        

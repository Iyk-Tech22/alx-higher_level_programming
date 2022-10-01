#!/usr/bin/python3
import calculator_1 as calc
import sys

# Basic Arithmethics
if __name__ == "__main__":
    filename = sys.argv[0]
    args = sys.argv[1:]
    if len(args) != 3:
        print("Usage: {:s} <a> <operator> <b> ".format(filename))
        exit(1)
    if args[1] not in "*/+-":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(args[0])
    b = int(args[2])
    func = (calc.mul, calc.div, calc.add, calc.sub)
    for opt, func in zip("*/+-", func):
        if opt == args[1]:
            print("{:d} {:s} {:d} = {:d}".format(a, opt, b, func(a, b)))

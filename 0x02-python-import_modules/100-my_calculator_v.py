#!/usr/bin/python3


# Basic calcaculator with arithmetic operations
if __name__ == "__main__":
    import sys
    import calculator_1
    args = sys.argv[1:]
    filename = sys.argv[0]
    if len(args) == 3:
        if args[1] == "*" or args[1] == "/" or\
           args[1] == "+" or args[1] == "-":
            oprand1 = int(args[0])
            oprand2 = int(args[2])
            if args[1] == "*":
                calc = calculator_1.mul(oprand1, oprand2)
            elif args[1] == "/":
                calc = calculator_1.div(oprand1, oprand2)
            elif args[1] == "+":
                calc = calculator_1.add(oprand1, oprand2)
            elif args[1] == "-":
                calc = calculator_1.sub(oprand1, oprand2)
            print("{:d} {:s} {:d} = {:d}".format(oprand1, args[1],
                                                 oprand2, calc))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: {:s} <a> <operator> <b>".format(filename))
        exit(1)

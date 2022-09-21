#!/usr/bin/python3


# print_last_digit: print the last digit of an interger
# @number: Interge to manupulate
# Return: last digit
def print_last_digit(number):
    last_digit = abs(number) % 10
    print("{:d}".format(last_digit), end="")
    return last_digit

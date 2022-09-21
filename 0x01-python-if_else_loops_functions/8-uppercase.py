#!/usr/bin/python3


# isupper: checks if a character is upper or not
def isupper(str):
    for char in str:
        to_ascii = ord(char)
        ascii_v = '';
        if to_ascii >= 97 and to_ascii <= 122:
             ascii_v = chr(to_ascii - 32)
        else:
            ascii_v = chr(to_ascii)
        print("{:s}".format(ascii_v), end="")
    print("") 

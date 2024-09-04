#!/usr/bin/python3

def uppercase(str):
    for char in str:
        # Check if character is a lowercase letter
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")

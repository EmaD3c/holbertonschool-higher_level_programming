#!/usr/bin/python3

def uppercase(str):
    for char in str:
        # Check if character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert to uppercase by subtracting 32 from ASCII value
            print(chr(ord(char) - 32), end='')
        else:
            # Print non-lowercase characters as they are
            print(char, end='')
            
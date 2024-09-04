#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if 97 <= ord(char) <= 122:  # Check if char is lowercase
            # Convert to uppercase
            char = chr(ord(char) - 32)
        # Print the character
        print(char, end="")
    print()  # Print a new line at the end

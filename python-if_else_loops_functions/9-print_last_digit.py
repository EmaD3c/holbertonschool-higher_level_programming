#!/usr/bin/python3
def print_last_digit(number):
    # Calculate the absolute value of the last digit
    value = abs(number) % 10
    # Print the last digit
    print(value, end='')
    return value

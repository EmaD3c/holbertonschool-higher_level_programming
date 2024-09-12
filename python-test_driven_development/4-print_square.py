#!/usr/bin/python3
"""
This module defines a function that prints a square using the character '#'.
It ensures that the size provided is a valid integer and handles exceptions
accordingly.

The function print_square(size):
- Prints a square of a given size.
- Raises TypeError if the size is not an integer.
- Raises ValueError if the size is less than 0.
"""


def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size (int): The size of the square to print.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)  # Print each line of the square

#!/usr/bin/python3
"""
Module 1-square
Defines a class Square with a private instance attribute 'size'.
"""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size):
        """Initializes the square with a private size attribute."""
        self.__size = size

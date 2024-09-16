#!/usr/bin/python3
"""
Module 4-square
Defines a square with private instance attribute 'size' and a getter/setter.
"""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """Initializes the square with an optional size."""
        self.size = size  # Use the setter to validate and set the size

    def size(self):
        """Getter method to retrieve the size."""
        return self.__size

    def size(self, value):
        """Setter method to set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Set the private size attribute

    def area(self):
        """Calculates the area of the square."""
        return self.__size * self.__size  # Return the area (size squared)

#!/usr/bin/python3
"""
Module 5-square
Defines a square with private instance attribute 'size' and a getter/setter.
Includes methods to calculate area and print the square using '#'.
"""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """Initializes the square with an optional size."""
        self.size = size  # Use the setter to validate and set the size

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size

    @size.setter
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

    def my_print(self):
        """Prints the square using the character '#'.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")  # Print an empty line if size is 0
        else:
            for i in range(self.__size):
                print("#" * self.__size)  # Print a square line-by-line

#!/usr/bin/python3
"""
Module 6-square
Defines a square with private attributes 'size' and 'position'.
Includes methods to calculate area and print the square using '#'.
"""


class Square:
    """Represents a square with private size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with optional size and position."""
        self.size = size        # Use the setter to validate and set the size
        # Use the setter to validate and set the position
        self.position = position

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
        self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the position with validation."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the character '#'.
        If size is 0, prints an empty line.
        Position is used to add leading spaces.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()  # Print leading empty lines based on position[1]
            for _ in range(self.__size):
                # Print each line with leading spaces
                print(" " * self.__position[0] + "#" * self.__size)

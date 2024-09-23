#!/usr/bin/python3
"""
Module 11-square
Defines the class Square that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that represents a Square, inherits from Rectangle"""

    def __init__(self, size):
        """
        Initialize the square with a size
        Size is validated by integer_validator from BaseGeometry
        """
        self.integer_validator("size", size)
        self.__size = size
        # Call the parent class constructor with size for width and height
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Returns a string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)

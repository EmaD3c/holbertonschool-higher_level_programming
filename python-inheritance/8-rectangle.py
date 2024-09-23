#!/usr/bin/python3
"""
Module 8-rectangle
Defines the class Rectangle that inherits from BaseGeometry.
"""
from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] {self.__width} / {self.__height}"

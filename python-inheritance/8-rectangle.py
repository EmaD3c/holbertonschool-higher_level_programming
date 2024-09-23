#!/usr/bin/python3
"""
Module 8-rectangle
Defines the class Rectangle that inherits BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """
    Class that represents a Rectangle, inherits from BaseGeometry
    """

    def __init__(self, width, height):

        """
        init width and height
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

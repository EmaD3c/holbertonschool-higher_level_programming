#!/usr/bin/python3
"""
Module 8-rectangle
Defines the class Rectangle that inherits from BaseGeometry.
"""


class BaseGeometry:
    """base geometry"""

    def area(self):
        """exception if area is not implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """is an integer?"""
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """ Rectangle"""

    def __init__(self, width, height):
        """initialization method"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

#!/usr/bin/python3
"""
Module base_geometry
Defines the class BaseGeometry with methods for area calculation and validation
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
        return value

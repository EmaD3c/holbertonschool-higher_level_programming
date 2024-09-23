#!/usr/bin/python3
"""
Module base_geometry
Defines the class BaseGeometry with methods for area calculation and validation.
"""


class BaseGeometry:
    """Class BaseGeometry."""

    def area(self):
        """Raises an Exception for unimplemented area method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value as a positive integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

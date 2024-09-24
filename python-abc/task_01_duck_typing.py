#!/usr/bin/python3
"""
Create an abstract class named Shape using the ABC package
Create two subclasses of Shape
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract class Shape"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle class inherits Shape"""

    def __init__(self, radius):
        """radius used to calculate both the area and the perimeter"""
        self.radius = abs(radius)

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return (2 * self.radius) * pi


class Rectangle(Shape):
    """Rectangle class inherits Shape"""

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


def shape_info(shape):
    """Print the area and perimeter of the shape passed to the function"""

    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))

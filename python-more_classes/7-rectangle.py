#!/usr/bin/python3
"""
Module 6-rectangle
Defines a rectangle
"""


class Rectangle:
    """
    Class that defines a rectangle.

    Attributes:
        number_of_instances (int): number of instances of the Rectangle
        print_symbol: symbol for string representation. Can be any type
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with optional width and height.
        Increments the number_of_instances when a new instance is created.

        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute. Validates the value.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute. Validates the value.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        Returns 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation of the rectangle
        using the character stored in print_symbol.
        If width or height is 0, return an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return (str(self.print_symbol) * self.__width + "\n") * self.__height

    def __repr__(self):
        """
        Return a string representation of the rectangle
        that can be used to recreate it.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted
        and decrements the number_of_instances.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

#!/usr/bin/python3
"""
This module defines the function say_my_name, which prints a formatted
string with the first and last name provided as arguments.
"""


def say_my_name(first_name, last_name=""):

    """
    Prints "My name is <first name> <last name>" with the given names.

    Args:
        first_name (str): The first name to print.
        last_name (str, optional): The last name to print.

    Raises:
        TypeError: If first_name or last_name is not a string.

    Example:
        say_my_name("John", "Smith")
        Output: My name is John Smith
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")

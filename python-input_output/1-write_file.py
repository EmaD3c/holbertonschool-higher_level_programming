#!/usr/bin/python3
"""
Module to write a string to a text file (UTF8)
and return the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)
    and returns the number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as text_file:
        return text_file.write(text)

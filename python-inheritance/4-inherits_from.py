#!/usr/bin/python3
"""
Module 4-inherits_from
Returns True if the object is an instance of a class that inherited (directly
or indirectly) from the specified class; otherwise False.
"""


def inherits_from(obj, a_class):
    """Returns True if obj inherits from a_class (but is not exactly a_class)"""
    return isinstance(obj, a_class) and type(obj) != a_class

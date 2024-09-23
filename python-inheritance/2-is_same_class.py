#!/usr/bin/python3
"""
Module 2-is_same_class
 returns True if the object is exactly an instance of the class
; otherwise False.
"""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class"""
    return type(obj) == a_class

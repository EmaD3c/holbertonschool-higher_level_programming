#!/usr/bin/python3
"""
Module 1-my_list
Write a class MyList that inherits from list
"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Prints the list, but sorted in ascending order"""
        print(sorted(self))

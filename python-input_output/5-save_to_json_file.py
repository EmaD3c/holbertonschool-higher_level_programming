#!/usr/bin/python3
"""
This module provides a function to save a Python object to a text file
using JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation.
    """
    with open(filename, 'w', encoding="utf-8") as text_file:
        # Write the JSON serialized object to the file
        json.dump(my_obj, text_file)

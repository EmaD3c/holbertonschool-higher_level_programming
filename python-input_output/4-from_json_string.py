#!/usr/bin/python3

"""
Function to convert a JSON string to a Python object.
"""
import json


def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.
    """
    # Use json.loads to convert the JSON string to a Python object.
    return json.loads(my_str)

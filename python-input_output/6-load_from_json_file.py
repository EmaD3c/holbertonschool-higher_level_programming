#!/usr/bin/python3
"""
This module provides a function to load a Python object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Loads an object from a JSON file.
    """
    with open(filename, 'r', encoding="utf-8") as text_file:
        # Use json.load() to parse the JSON content
        return json.load(text_file)

#!/usr/bin/python3
"""
serialization module that adds a functionality to serialize a Python dictionary
to a JSON file and deserialize the JSON file to recreate the Python Dictionary.
"""

import json
import os


def serialize_and_save_to_file(data, filename):
    """
    Serializes Python dictionary 'data',saves it to the specified
    JSON file 'filename'
    If the file already exists, it will be replaced.

    Args:
        data (dict): The dictionary to serialize and save.
        filename (str): The name of the file where the data will be saved.
    """

    # Check if file exists, and remove it if necessary
    if os.path.exists(filename):
        os.remove(filename)

    # Open the file and write serialized JSON data
    with open(filename, 'w') as file:
        json_data = json.dumps(data)  # Serialize data to JSON format
        file.write(json_data)


def load_and_deserialize(filename):
    """
    Loads and deserializes data from the specified JSON file 'filename'
    into a Python dictionary.

    Args:
        filename (str): The name of the file to load data from.

    Returns:
        dict: The deserialized Python dictionary from the file.
    """

    # Open the file and deserialize JSON back to Python dictionary
    with open(filename, 'r') as file:
        data = json.load(file)

    return data

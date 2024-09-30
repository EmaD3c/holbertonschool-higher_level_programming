#!/usr/bin/python3
"""
Defines a Student class
"""


class Student:
    """A class that defines a student by first name, last name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initializes the student with first_name, last_name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only those attributes are retrieved.
        Otherwise, all attributes are retrieved.

        Args:
            attrs (list): A list of attribute names to retrieve (optional).

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__

        # Filter and return only the attributes in the provided list
        return {attr: self.__dict__[attr] for attr in attrs if attr in self.__dict__}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from json.

        Args:
            json (dict): A dictionary containing the new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)

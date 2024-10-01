#!/usr/bin/python3
"""
 serialize and deserialize custom Python objects using the pickle module.
"""
import pickle


class CustomObject:
    """
    A class that represents an object with name, age, and is_student attributes
    """

    def __init__(self, name, age, is_student):
        """Initializes the object with name, age, and is_student attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the attributes of the object."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance and saves it to the specified filename
        """
        try:
            # wb = write binary (écriture binaire)
            with open(filename, "wb") as file:
                pickle.dump(self, file)  # Serialize the object
        except Exception as e:
            print(f"Error serializing object: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Loads, returns an instance of CustomObject from the specified filename
        """
        try:
            # rb = read binary (lecture binaire)
            with open(filename, "rb") as file:
                loaded_self = pickle.load(file)  # Deserialize the object
                return loaded_self  # Return the deserialized object
        except Exception as e:
            print(f"Error deserializing object: {e}")
            return None

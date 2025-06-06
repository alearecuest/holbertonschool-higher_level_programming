#!/usr/bin/env python3
"""
This module implements a custom object class that can be
serialized and deserialized using the pickle module.
"""

import pickle


class CustomObject:
    """
    A custom class with attributes for name, age, and student status,
    which can be serialized and deserialized using pickle.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject with name, age, and student status.

        Args:
            name: A string representing the name
            age: An integer representing the age
            is_student: A boolean indicating whether the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in a formatted manner.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")


def serialize(self, filename):
    """
    Serialize the current instance and save it to a file.
    Args:
        filename: The name of the file to save the serialized object to
    """
    try:
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
    except Exception:
        return None


@classmethod
def deserialize(cls, filename):
    """
    Load and return an instance of CustomObject from a file.

    Args:
        filename: The name of the file containing the serialized object

    Returns:
        An instance of CustomObject if successful, None otherwise
    """
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except (FileNotFoundError, pickle.PickleError):
        return None

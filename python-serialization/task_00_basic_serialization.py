#!/usr/bin/env python3
"""
This module provides basic serialization and deserialization
functionality for Python dictionaries to JSON files and vice versa.
"""

import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to JSON format and saves it to a file.

    Args:
        data: A Python dictionary containing the data to be serialized
        filename: The name of the file where the JSON data will be saved
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Loads JSON data from a file and deserializes it into a Python dictionary.

    Args:
        filename: The name of the file containing JSON data to be loaded

    Returns:
        A Python dictionary containing the deserialized data from the JSON file
    """
    with open(filename, 'r') as file:
        return json.load(file)

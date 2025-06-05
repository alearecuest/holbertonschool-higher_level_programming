#!/usr/bin/python3
"""
Module for saving Python objects to files using JSON representation.
This module provides functionality to serialize Python objects to JSON
and save them to files.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using JSON representation.

    This function serializes the given object to JSON format and writes
    it to the specified file. It uses the 'with' statement to ensure
    proper file handling.

    Args:
        my_obj: The Python object to be serialized and saved
        filename (str): The name of the file to save the JSON to

    Returns:
        None
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

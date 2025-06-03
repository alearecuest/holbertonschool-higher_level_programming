#!/usr/bin/python3
"""
This module provides functionality for JSON serialization.
It contains a function that converts a Python object to its
JSON string representation.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON string representation of an object.

    This function takes a Python object and converts it to
    a JSON formatted string using the json module.

    Args:
        my_obj: The Python object to be converted to JSON string

    Returns:
        str: A JSON formatted string representation of the object

    Note:
        - Does not handle exceptions if the object can't be serialized
        - Common serializable types include:
            dict, list, str, int, float, bool, None
        - Non-serializable types (like sets) will raise TypeError
    """
    return json.dumps(my_obj)

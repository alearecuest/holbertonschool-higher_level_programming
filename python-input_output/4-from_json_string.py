#!/usr/bin/python3
"""
Module that contains a function to convert a
JSON string to a Python object.
"""
import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    This function takes a JSON formatted string and converts it
    to the corresponding Python data structure (such as list,
    dictionary, string, integer, etc.)

    Args:
        my_str (str): The JSON string to be converted

    Returns:
        The Python data structure represented by the JSON string.
        Could be a dictionary, list, string, integer, etc.
        depending on the input JSON.
    """
    return json.loads(my_str)

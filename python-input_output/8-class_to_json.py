#!/usr/bin/python3
"""
Module that defines a function to convert a class instance to a
JSON-serializable dictionary.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object.

    Args:
        obj: An instance of a Class

    Returns:
        A dictionary containing all serializable attributes of the object
    """
    return obj.__dict__

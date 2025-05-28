#!/usr/bin/python3
"""
Module that contains the lookup function.
This module provides a way to get all attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    Args:
        obj: The object to inspect

    Returns:
        A list of strings with the names of attributes and methods
    """
    return dir(obj)

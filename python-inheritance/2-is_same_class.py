#!/usr/bin/python3
"""
Module that contains the is_same_class function.
This module provides a way to check if an object is exactly an instance
of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class;
    otherwise False.
    Args:
        obj: The object to check
        a_class: The class to compare against
    Returns:
        True if obj is exactly an instance of a_class, otherwise False
    """
    return type(obj) is a_class

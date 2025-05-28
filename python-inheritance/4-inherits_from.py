#!/usr/bin/python3
"""
Module that contains the inherits_from function.
This module provides a way to check if an object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        True if obj is an instance of a subclass of a_class, otherwise False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

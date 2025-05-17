#!/usr/bin/python3
"""
Module for adding integers

This module provides a function that adds two integers together.
The function handles type validation and conversion.
"""


def add_integer(a, b=98):
    """
    Adds two integers and returns the result.

    Args:
        a: first number (must be int or float)
        b: second number (must be int or float), defaults to 98

    Returns:
        int: sum of a and b after casting to integers

    Raises:
        TypeError: if a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

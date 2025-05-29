#!/usr/bin/python3
"""
Module that defines the BaseGeometry class.
This module provides a base class for geometry-related classes.
"""


class BaseGeometry:
    """
    BaseGeometry class with area method.
    This class serves as a base for geometry-related classes.
    """
    def area(self):
        """
        Calculates the area of a geometric shape.
        This method must be implemented by derived classes.

        Raises:
            Exception: Always raises an Exception with the message
                      'area() is not implemented'
        """
        raise Exception("area() is not implemented")

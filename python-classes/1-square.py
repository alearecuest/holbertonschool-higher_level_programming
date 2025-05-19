#!/usr/bin/python3
"""
This module defines a Square class.
This module provides a simple Square class with a private instance attribute.
"""


class Square:
    """
    A class that defines a square.
    This class represents a square geometric shape and stores its
    size as a private attribute.
    Attributes:
    __size (int): The size of the square (private attribute)
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.
        Args:
        Size: The size of the square (no type/value verification)
        """
        self.__size = size

#!/usr/bin/python3
"""
This module defines a Square class.
This module provides a Square class with size validation and area calculation.
"""


class Square:
    """
    A class that defines a square.
    This class represents a square with size validation and
    can calculate its area.
    Attributes:
        __size (int): The size of the square (private attribute)
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.
        Args:
            size (int, optional): The size of the square. Defaults to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.
        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2

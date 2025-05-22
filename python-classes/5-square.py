#!/usr/bin/python3
"""
This module defines a Square class.
This module provides a Square class with properties for size manipulation,
area calculation and printing capabilities.
"""


class Square:
    """
    A class that defines a square.
    This class represents a square with controlled access to size attribute,
    can calculate its area and print its representation.
    Attributes:
        __size (int): The size of the square (private attribute)
    """
    def __init__(self, size=0):
        """
        Initialize a new Square instance.
        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.
        Args:
            value (int): The new size of the square.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.
        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the character #.
        If size is equal to 0, print an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

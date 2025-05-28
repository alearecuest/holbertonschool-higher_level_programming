#!/usr/bin/python3
"""
Module that contains the MyList class.
This module provides a class that inherits from list with additional functionality.
"""


class MyList(list):
    """
    MyList class that inherits from list.
    This class extends the built-in list class with additional methods.
    """
    def print_sorted(self):
        """
        Prints the list sorted in ascending order.
        All elements are assumed to be of type int.
        """
        print(sorted(self))

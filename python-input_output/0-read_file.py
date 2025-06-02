#!/usr/bin/env python3
"""
This module provides functionality for file I/O operations in Python.
It contains a function to read text files and display their contents
to standard output without any modifications.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.
    This function opens the specified file with proper UTF-8 encoding,
    reads all its contents at once, and prints them to standard output
    without adding any extra newlines.

    Args:
        filename (str): The name/path of the file to be read.
                        Defaults to an empty string.

    Returns:
        None: The function prints to stdout but doesn't return any value

    Note:
        - Uses the 'with' statement to ensure proper file handling
        - Does not handle exceptions for file permissions or missing files
        - Prints content exactly as it appears in the file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")

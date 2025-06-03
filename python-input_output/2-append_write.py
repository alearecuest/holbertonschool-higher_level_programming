#!/usr/bin/python3
"""
This module provides functionality for appending text to files.
It contains a function that adds a string to the end of a text file
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8) and returns
    the number of characters added.

    This function opens the specified file with UTF-8 encoding
    in append mode, which creates the file if it doesn't exist.
    It then adds the provided text to the end of the file and
    returns the character count.

    Args:
        filename (str): The name/path of the file. Defaults to
                       an empty string.
        text (str): The text to append to the file. Defaults to
                   an empty string.

    Returns:
        int: The number of characters added to the file

    Note:
        - Uses the 'with' statement to ensure proper file handling
        - Creates the file if it doesn't exist
        - Appends the content to the end if the file already exists
        - Does not handle file permission exceptions
    """
    with open(filename, 'a', encoding="utf-8") as f:
       return f.write(text)

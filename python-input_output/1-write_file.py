#!/usr/bin/python3
"""
This module provides functionality for writing text to files.
It contains a function that writes a string to a text file and
returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number
    of characters written.

    This function opens the specified file with proper UTF-8 encoding
    in write mode, which creates the file if it doesn't exist or
    truncates it if it does exist. It then writes the provided text
    to the file and returns the character count.

    Args:
        filename (str): The name/path of the file to write to. Defaults to
                       an empty string.
        text (str): The text to write to the file. Defaults to an empty string.

    Returns:
        int: The number of characters written to the file

    Note:
        - Uses the 'with' statement to ensure proper file handling
        - Creates the file if it doesn't exist
        - Overwrites the content if the file already exists
        - Does not handle file permission exceptions
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)

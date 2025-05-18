#!/usr/bin/python3
"""
Module that provides a function for text indentation.

This module contains a function that formats text by adding
new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be printed with indentation.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        
        if text[i] in [".", "?", ":"]:
            print("\n\n", end="")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue

        i += 1

#!/usr/bin/python3
"""
Module for loading Python objects from JSON files.
This module provides functionality to deserialize JSON data from
files into Python objects.
"""
import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    This function reads a JSON file and converts its contents to
    a Python object. It uses the 'with' statement to ensure proper
    file handling.

    Args:
        filename (str): The name of the file to read the JSON from

    Returns:
        The Python object represented by the JSON in the file.
        Could be a dictionary, list, string, integer, etc.
        depending on the JSON content.
    """
    with open(filename, 'r') as f:
        return json.load(f)

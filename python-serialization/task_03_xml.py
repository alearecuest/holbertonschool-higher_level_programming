#!/usr/bin/env python3
"""
This module provides functionality to serialize and deserialize
Python dictionaries to XML format.
"""

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to XML format and saves it to a file.

    Args:
        dictionary: The Python dictionary to serialize
        filename: The name of the file to save the XML data
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
    Reads XML data from a file and deserializes it into a Python dictionary.

    Args:
        filename: The name of the file containing XML data

    Returns:
        A Python dictionary containing the deserialized data
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        result[child.tag] = child.text

    return result

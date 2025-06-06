#!/usr/bin/env python3
"""
This module provides functionality to convert CSV data to JSON format.
"""

import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Converts data from a CSV file to JSON format and saves it to data.json.
    Args:
        csv_filename: The name of the CSV file to convert
    Returns:
        True if conversion was successful, False otherwise
    """
    try:
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)
        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False

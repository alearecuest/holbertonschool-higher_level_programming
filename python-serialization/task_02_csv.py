#!/usr/bin/env python3
"""
This module provides functionality to convert CSV data to JSON format.
"""

import csv
import json
import os

def convert_csv_to_json(csv_filename):
    """
    Converts data from a CSV file to JSON format and saves it to data.json.
    Args:
        csv_filename: The name of the CSV file to convert
    Returns:
        True if conversion was successful, False otherwise
    """
    try:
        if not os.path.exists(csv_filename):
            with open('data.json', 'w') as json_file:
                json.dump([], json_file)
            return False

        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True

    except Exception as e:
        with open('data.json', 'w') as json_file:
            json.dump([], json_file)
        return False

#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_ordered_list(self):
        """Test with an ordered list of integers"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers"""
        unordered = [1, 3, 4, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """Test with list where max value is at the beginning"""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test with a list containing a single element"""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Test with a list of floats"""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Test with a list containing both integers and floats"""
        mixed = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(mixed), 15.5)

    def test_string(self):
        """Test with a string"""
        string = "Holberton"
        self.assertEqual(max_integer(string), 't')

    def test_list_of_strings(self):
        """Test with a list of strings"""
        strings = ["Holberton", "School", "is", "cool"]
        self.assertEqual(max_integer(strings), "is")

    def test_empty_string(self):
        """Test with an empty string"""
        self.assertEqual(max_integer(""), None)

    def test_negative_numbers(self):
        """Test with list of negative numbers"""
        negatives = [-2, -6, -1, -9]
        self.assertEqual(max_integer(negatives), -1)
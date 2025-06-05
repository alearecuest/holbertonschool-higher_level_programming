#!/usr/bin/python3
"""
Module for Student class
"""


class Student:
    """
    Class that defines a student.

    Attributes:
        first_name (str): The first name of the student
        last_name (str): The last name of the student
        age (int): The age of the student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of strings representing attribute
                names to include in the returned dictionary. If None, all
                attributes are included.

        Returns:
            dict: A dictionary containing the requested attributes
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__

        filtered_dict = {}
        for attr in attrs:
            if isinstance(attr, str) and hasattr(self, attr):
                filtered_dict[attr] = getattr(self, attr)

        return filtered_dict

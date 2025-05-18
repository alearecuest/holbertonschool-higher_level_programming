#!/usr/bin/python3
"""
Module for matrix division

This module provides a function that divides all elements
of a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float) to divide by.

    Returns:
        A new matrix with all elements divided by div and rounded
        to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                  if rows have different sizes, or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(
            isinstance(element, (int, float))
               for row in matrix for element in row):
       raise TypeError(
           "matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix) > 0:
        row_size = len(matrix[0])
        if not all(len(row) == row_size for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix

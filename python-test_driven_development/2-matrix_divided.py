#!/usr/bin/python3
"""Divides all elements of a matrix by div and returns
a new matrix with elements rounded to 2 decimal places."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists): A list of lists of integers or floats.
        div (int or float): The number by which to divide all matrix elements.

    Returns:
        list of lists: A new matrix with elements divided by div, rounded
        to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if the rows of the matrix are not the same size,
                   or if div is not a number (integer or float).
        ZeroDivisionError: If div is zero.
    """

    # Error message to be used in multiple places
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check if matrix is a list of lists and not empty
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(error_msg)

    # Initialize the length of the first row
    line_len = None

    # Validate each row in the matrix
    for line in matrix:
        # Check if each row is a list and not empty
        if not isinstance(line, list) or len(line) == 0:
            raise TypeError(error_msg)

        # Check if all rows have the same length
        if line_len is None:
            line_len = len(line)
        elif len(line) != line_len:
            raise TypeError("Each row of the matrix must have the same size")

        # Check if all elements in each row are either integers or floats
        for num in line:
            if not isinstance(num, (int, float)):
                raise TypeError(error_msg)

    # Return new matrix with each element divided by div and to 2 decimal place
    return [[round(num / div, 2) for num in line] for line in matrix]

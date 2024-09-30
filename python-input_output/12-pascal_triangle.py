#!/usr/bin/python3
"""
Defines a function to create Pascal's triangle
"""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of n."""
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    triangle = []  # Initialize the list to hold the rows of the triangle

    for i in range(n):
        # Create a new row with 1's
        row = [1] * (i + 1)

        # Calculate the values for the interior elements of the row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)  # Append the completed row to the triangle

    return triangle  # Return the completed triangle

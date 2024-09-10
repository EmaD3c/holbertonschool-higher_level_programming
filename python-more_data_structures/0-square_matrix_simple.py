#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Use list comprehension to create a new matrix
    new_matrix = [[element ** 2 for element in row] for row in matrix]

    return new_matrix

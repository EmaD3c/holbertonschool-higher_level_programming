#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Use list comprehension to create a new matrix
    return [[element ** 2 for element in row] for row in matrix]

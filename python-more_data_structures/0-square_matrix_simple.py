#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Use list comprehension to create a new matrix
    new_matrix = [[element ** 2 for element in line] for line in matrix]

    return new_matrix

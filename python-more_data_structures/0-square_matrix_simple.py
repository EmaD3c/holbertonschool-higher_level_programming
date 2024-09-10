#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Initialize an empty list to hold the squared values
    ret = []

    # Loop through each row in the matrix
    for row in matrix:
        # Square each element in the row and create a new row
        squared_row = [x ** 2 for x in row]

        # Append the squared row to the result list
        ret.append(squared_row)

    # Return the new matrix with squared values
    return ret

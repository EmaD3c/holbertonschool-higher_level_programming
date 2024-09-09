#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j < len(matrix[i]) - 1:
                # Imprime l'élément avec un espace sauf le dernier de la ligne
                print("{:d}".format(matrix[i][j]), end=" ")
            else:
                # Imprime le dernier élément sans espace à la fin
                print("{:d}".format(matrix[i][j]))
        if len(matrix[i]) == 0:
            # Si la ligne est vide, imprime simplement une ligne vide
            print()

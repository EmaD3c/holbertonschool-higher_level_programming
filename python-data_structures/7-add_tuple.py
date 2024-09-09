#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ajouter des valeurs par défaut (0) si les tuples ont moins de 2 éléments
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # Additionner les deux premiers éléments des deux tuples
    sum_1 = tuple_a[0] + tuple_b[0]
    sum_2 = tuple_a[1] + tuple_b[1]

    # Retourner le résultat sous forme d'un nouveau tuple
    return (sum_1, sum_2)

#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    # Initialiser max_val avec le premier élément de la liste
    max = my_list[0]
    for i in my_list:
        # Comparer chaque élément avec max_val
        if i > max:
            # Mettre à jour max_val si un élément est plus grand
            max = i

    return max

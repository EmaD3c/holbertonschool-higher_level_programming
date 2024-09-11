#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            # Vérifie si l'élément à l'index i est un entier
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
    except IndexError:
        # Gérez le cas où x est plus grand que la longueur de la liste
        pass
    print()
    return count

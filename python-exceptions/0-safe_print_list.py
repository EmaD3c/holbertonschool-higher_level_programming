#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            count += 1
    except IndexError:
        # Gérez le cas où x est plus grand que la longueur de la liste
        pass
    print()  # Imprime une nouvelle ligne après les éléments imprimés
    return count

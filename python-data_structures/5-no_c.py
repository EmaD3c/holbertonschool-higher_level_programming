#!/usr/bin/python3
def no_c(my_string):
    # Créer une nouvelle chaîne sans les caractères 'c' et 'C'
    new_string = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            new_string += i
    return new_string

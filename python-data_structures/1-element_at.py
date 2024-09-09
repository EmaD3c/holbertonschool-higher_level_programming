#!/usr/bin/python3
def element_at(my_list, idx):
    # Vérifier si l'index est négatif
    if idx < 0:
        return None
    # Vérifier si l'index dépasse la taille de la liste
    if idx >= len(my_list):
        return None
    # Retourner l'élément à l'index donné
    return my_list[idx]

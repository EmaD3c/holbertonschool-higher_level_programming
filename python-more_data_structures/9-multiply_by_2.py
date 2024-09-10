#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Créer un nouveau dictionnaire pour stocker les résultats
    new_dict = {}
    # Parcourir les clés et valeurs du dictionnaire
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    return new_dict

#!/usr/bin/python3
def best_score(a_dictionary):
    # Vérifier si le dictionnaire est vide ou None
    if not a_dictionary:
        return None

    # Utilise la fonction max pour trouver la clé avec la valeur la plus élevée
    max_key = max(a_dictionary, key=a_dictionary.get)

    return max_key

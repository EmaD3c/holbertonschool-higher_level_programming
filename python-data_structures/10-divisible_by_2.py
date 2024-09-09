#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Créer une nouvelle liste pour stocker True ou False
    result = []

    # Parcourir chaque élément de la liste originale
    for i in my_list:
        # Ajouter True si l'élément est divisible par 2, sinon ajouter False
        if i % 2 == 0:
            result.append(True)
        else:
            result.append(False)

    # Retourner la nouvelle liste contenant True ou False
    return result

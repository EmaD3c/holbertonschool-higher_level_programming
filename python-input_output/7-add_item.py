#!/usr/bin/python3
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Essayer de charger le fichier s'il existe, sinon initialiser une liste vide
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Ajouter les nouveaux arguments à la liste (ignorer le nom du script)
my_list.extend(sys.argv[1:])

# Sauvegarder la liste mise à jour dans le fichier JSON
save_to_json_file(my_list, filename)

#!/usr/bin/python3
"""
reading data from one format (CSV) and converting it
into another format (JSON) using serialization techniques
"""

import json
import csv


def convert_csv_to_json(csv_filename):
    """
    take the CSV filename as its parameter and write the JSON data to data.json
    """
    try:
        # Ouvre le fichier CSV en mode lecture
        with open(csv_filename, mode='r') as csv_file:
            # Use DictReader pour lire le fichier CSV en tant que dictionnaire
            csv_reader = csv.DictReader(csv_file)

            # Convertir les lignes du fichier CSV en une liste de dictionnaires
            data = [row for row in csv_reader]

        # Sérialise la liste de dictionnaire en JSON et l'écrire dans data.json
        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        # Si le fichier CSV n'est pas trouvé, retourner False
        print(f"Error: The file {csv_filename} was not found.")
        return False
    except Exception as e:
        # Si une autre erreur se produit, retourner False et afficher l'erreur
        print(f"An error occurred: {e}")
        return False

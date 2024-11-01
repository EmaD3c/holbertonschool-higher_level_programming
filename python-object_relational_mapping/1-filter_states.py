#!/usr/bin/python3
"""
Liste tous les états de la base de données hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Récupérer les arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Se connecter à la base de données MySQL
    dataB = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Créer un curseur pour exécuter des commandes SQL
    cursor = dataB.cursor()

    # Récupérer tous les états commençant par 'N', triés par ID
    cursor.execute("SELECT * FROM states WHERE name\
    LIKE BINARY 'N%' ORDER BY id ASC")

    # Récupérer tous les résultats de la requête
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    dataB.close()

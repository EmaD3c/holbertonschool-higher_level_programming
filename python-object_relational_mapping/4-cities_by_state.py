#!/usr/bin/python3
"""
Liste toutes les villes de la base de données hbtn_0e_4_usa
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

    # Exécuter la requête SQL pour récupérer toutes les villes avec le nom de l'état
    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    # Récupérer tous les résultats de la requête
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    dataB.close()

#!/usr/bin/python3
"""
Liste toutes les villes de la base de données hbtn_0e_4_usa pour un état donné
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Récupérer les arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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

    # Requête SQL pour récupérer toutes les villes avec le nom de l'état
    cursor.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (state_name,))

    # Récupérer tous les résultats de la requête
    cities = cursor.fetchall()

    # Extraire les noms des villes et les afficher sous forme de chaîne
    city_names = [city[0] for city in cities]
    print(", ".join(city_names))

    cursor.close()
    dataB.close()

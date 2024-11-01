#!/usr/bin/python3
"""
Affiche tous les objets State
contenant la lettre 'a' dans la base de données hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Récupérer les arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Créer l'engine pour se connecter à la base de données
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Créer une session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Appliquer le filtre pour les noms contenant 'a'
    name_filter = State.name.like('%a%')

    # Récupérer les objets State avec la lettre 'a' dans le nom, triés par id
    states_with_a = session.query(State).filter(name_filter) \
        .order_by(State.id).all()

    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    session.close()

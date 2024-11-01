#!/usr/bin/python3
"""
Affiche le premier objet State de la base de données hbtn_0e_6_usa
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
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (username, password, database), pool_pre_ping=True)

    # Créer une session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupérer le premier objet State trié par id
    first_state = session.query(State).order_by(State.id).first()

    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    session.close()

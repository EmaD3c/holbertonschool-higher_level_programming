#!/usr/bin/python3
"""
Prints all City objects from the database, sorted by `cities.id`.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the engine to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to retrieve all cities, joined with their corresponding states
    rows = session.query(City, State).join(State).order_by(City.id).all()
    for city, state in rows:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()

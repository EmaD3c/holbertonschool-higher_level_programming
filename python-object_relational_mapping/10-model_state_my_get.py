#!/usr/bin/python3
"""
Finds the State object with the specified name from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Retrieve arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Create an engine to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the State object by name (SQL injection-safe)
    state = session.query(State).filter(State.name == state_name).first()

    # Display results
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    # Close the session
    session.close()

#!/usr/bin/python3
"""
Adds the State object “Louisiana” to the database hbtn_0e_6_usa
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

    # Create an engine to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object with the name "Louisiana"
    new_state = State(name="Louisiana")
    session.add(new_state)  # Add the new state to the session
    session.commit()  # Commit the transaction to save the state into database

    # Print the new state's ID after it has been saved to the database
    print("{}".format(new_state.id))

    # Close the session
    session.close()

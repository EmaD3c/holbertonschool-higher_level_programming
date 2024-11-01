#!/usr/bin/python3
"""Define a State class and the MySQL connection setup using SQLAlchemy."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base instance
Base = declarative_base()


class State(Base):
    """Represents the states table in the database."""

    __tablename__ = 'states'  # Name of the table

    # Define columns
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

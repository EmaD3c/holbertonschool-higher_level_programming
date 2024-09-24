#!/usr/bin/python3
"""
Create an iter class that extends the Python list class
"""


class CountedIterator:
    """an iter class CountedIterator"""

    def __init__(self, data):
        self.iterator = iter(data)  # iter() pour créer un itérateur
        self.count = 0

    def __iter__(self):
        return self  # Return the iterator object itself

    def __next__(self):
        self.count += 1  # Incrémente le compteur à chaque appel
        return next(self.iterator)  # Récupère le next élément de l'itérateur

    def get_count(self):
        return self.count

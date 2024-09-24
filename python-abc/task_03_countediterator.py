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
        # si une exception est levée par next(self.iterator)
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            # le bloc de code qui suit cette ligne sera exécuté.
            raise StopIteration

    def get_count(self):
        return self.count

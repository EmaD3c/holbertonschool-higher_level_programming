#!/usr/bin/python3
"""
Create a list class that extends the Python list class
"""


class VerboseList(list):
    """list class VerboseList"""

    def append(self, item):
        """append method"""
        super().append(item)  # Appeler la méthode d'origine
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """extend method"""
        super().extend(iterable)  # Appeler la méthode d'origine
        print(f"Extended the list with {len(iterable)} items.")

    def remove(self, item):
        """remove method"""
        print(f"Removing {item} from the list.")  # Message avant suppression
        super().remove(item)  # Appeler la méthode d'origine

    def pop(self, index=-1):
        """pop method"""
        item = super().pop(index)  # Appeler la méthode d'origine
        print(f"Popped {item} from the list.")  # Message après suppression

        return item

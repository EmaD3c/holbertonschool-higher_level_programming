#!/usr/bin/python3
"""
Create an iter class
"""


class SwimMixin:
    """a class SwimMixin"""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """a class FlyMixin"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """a class  that inherits from both SwimMixin and FlyMixin"""

    def roar(self):
        print("The dragon roars!")

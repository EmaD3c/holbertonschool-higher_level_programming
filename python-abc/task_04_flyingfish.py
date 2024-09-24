#!/usr/bin/python3
"""
Create an iter class that inherits from both a Fish class and a Bird
"""


class Fish:
    """a class FlyingFish"""

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """a class Bird"""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Bird, Fish):
    """FlyingFish class that inherits from both Fish and Bird """

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")

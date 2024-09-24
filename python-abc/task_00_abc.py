#!/usr/bin/env python3
"""
Create an abstract class named Animal using the ABC package
Create two subclasses of Animal: Dog and Cat. Implement the sound
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class Animal"""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented in subclasses"""
        pass


class Dog(Animal):
    """Dog class inherits from Animal and implements sound method"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class inherits from Animal and implements sound method"""

    def sound(self):
        return "Meow"

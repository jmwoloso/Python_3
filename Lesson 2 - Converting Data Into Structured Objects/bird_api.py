#!/usr/bin/python
#
# Program Demonstrating API Construction
#    bird_api.py
#
# Created by: Jason Wolosonovich
#    6/02/2015
#
# Lesson 2 - Exercise 2
"""
bird_api.py: API for software birds carrying objects.

@author: Jason M. Wolosonovich
"""
from bunchclass import Bunch

class Bird(Bunch):
    
    def pretty(self):
        """
        Replacement pretty() method
        """
        return "pretty bird!"
    
    
    def add(self, name, value):
        """
        Add an object for the Bird to carry in its basket.
            Name is what you call the object.
            Value is the actual object being placed in the basket.
        """
        if hasattr(self, 
                   name):
            raise KeyError("'{0}' object cannot be placed in basket".format(self.name))
        else:
            setattr(self, 
                    name, 
                    value)
    
        
    def remove(self, name):
        """
        Remove an object from the basket.
            Name is the string of the object to be removed.
        """
        if name in self.__dict__:
            delattr(self,
                    name)
        else:
            raise KeyError("'{0}' object not found in basket".format(self.name, ))
    
        
    def calculate(self):
        """
        Calculate the speed of the bird.
            Algorithm: 100 - (number of objects in the basket * 10),
                              minimum of 0.
            Results cannot be less than zero.
        """
        return max(100 - len(self.__dict__) * 10, 0)
    
    
    def basket(self):
        """
        Print the list of objects in the basket in an attractive format.
        """
        return "Basket Objects\n" + self.pretty()
    
    
if __name__=="__main__":
    swallow = Bird(fruit=("coconut", "orange"), drink="apple juice")
    swallow.add("cars", 3)
    print(swallow.basket())
    print(swallow.calculate())
    swallow.remove("drink")
    print(swallow.basket())
    print(swallow.calculate())
#!/usr/bin/python
#
# Program To Track Different Types Of Coconuts From Around The World
#    coconuts.py
#
# Created by: Jason M Wolosonovich
#    6/02/2015
#
# Lesson 2 - Project Attempt 1
"""
coconuts.py: A program that uses an inventory class to track different
             types of coconuts from around the world.

@author: Jason M. Wolosonovich
"""


class Coconut(object):
    # mangling these
    __weights = {'south asian': 3.0,
                 'middle eastern': 2.5,
                 'american': 3.5}
    
    def __init__(self, variety):
        """
        Instantiates a coconut class of the specified variety
        """
        # Check that variety of coconut is valid
        if variety.lower() not in self.__weights.keys():
            raise AttributeError("'variety' should one of "\
                                 "<'south asian', 'middle eastern', "\
                                 "'american'>")
        else:
            # variety is valid, set instance attributes
            # mangle attributes to prevent changes
            self.__variety = variety.lower()
            self.__weight = self.__weights[self.__variety]
    
    
                         
class Inventory(object):
    # mangle this   
    __summed_weight = float()
    
    def add_coconut(self, coconut):
        """
        Adds a coconut to the inventory
        """
        if not isinstance(coconut, Coconut):
            raise AttributeError("'{0}' must be an instance of class <cocnuts.Coconut>".format(coconut))
        self.__summed_weight += coconut._Coconut__weight
        print("\nCoconut added to inventory.")
         
    def total_weight(self):
        """
        Stores the total weight of the coconuts in inventory at any one time
        """
        return self.__summed_weight
    
    
if __name__=="__main__":
    c = Coconut('SOUTH ASIAN')
    # just to verify creation once; don't want these messed with normally
    print(c._Coconut__variety)
    print(c._Coconut__weight)
    i = Inventory()
    i.add_coconut(c)
    print(i.total_weight())
    d = Coconut('aMERICAN')
    i.add_coconut(d)
    print(i.total_weight())
           
#!/usr/bin/python
#
# Program To Track Different Types Of Coconuts From Around The World
#    coconuts.py
#
# Created by: Jason M Wolosonovich
#    6/04/2015
#
# Lesson 2 - Project Attempt 2
"""
coconuts.py: A program that uses an inventory class to track different
             types of coconuts from around the world.

@author: Jason M. Wolosonovich
"""


class Coconut(object):
    pass

class South_Asian(Coconut):
    def __init__(self):
        self.weight = 3.0

class Middle_Eastern(Coconut):
    def __init__(self):
        self.weight = 2.5
        
class American(Coconut):
    def __init__(self):
        self.weight = 3.5
    
                         
class Inventory(object):
    
    def __init__(self):
        self.nuts = []
    
    def add_coconut(self, coconut):
        """
        Adds a coconut to the inventory
        """
        # check for coconut instance
        if not isinstance(coconut, Coconut):
            raise AttributeError("'{0}' must be an instance of class <cocnuts.Coconut>".format(coconut))
        self.nuts.append(coconut)
        print("\n{0} Coconut added to inventory.".format(coconut.__class__.__name__))
         
    def total_weight(self):
        """
        Stores the total weight of the coconuts in inventory at any one time
        """
        return "Total weight: {0}".format(sum([nut.weight for nut in self.nuts]))
    
    
if __name__=="__main__":
    c = South_Asian()
    # verify creation one time
    print(c.__class__.__name__)
    print(c.weight)
    
    # create inventory and add coconuts
    i = Inventory()
    i.add_coconut(c)
    print(i.total_weight())
    
    d = American()
    i.add_coconut(d)
    print(i.total_weight())
    
    e = Middle_Eastern()
    i.add_coconut(e)
    print(i.total_weight())
    
    
           
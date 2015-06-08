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
        
    weights = {'south asian': 3.0,
               'middle eastern': 2.5,
               'american': 3.5}
    
    def __init__(self, variety):
        """
        Instantiates a coconut class of the specified variety
        Variety can be one of 'south asian', 'middle eastern' or 'american'
        """
                
        # if one of the allow varieties is specified, create that
        # type of coconut and assign the correct weight
        if variety.lower() in self.weights.keys():
            
            self.variety = variety.lower()
            self.weight = self.weights[variety]
                
        
                   
        
    
if __name__=="__main__":
    c = Coconut('mexican')
    print(c.variety)
    print(c.weight)
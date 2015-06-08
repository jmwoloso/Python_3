#!/usr/bin/python
#
# Test Suite For furnishings.py
#    test_furnishings.py
#
# Created by: Jason M Wolosonovich
#    6/04/2015
#
# Lesson 7 - Project Attempt 1
"""
test_furnishings.py: Test suite for furnishings.py

@author: Jason M. Wolosonovich
"""
import unittest
from furnishings import Sofa, Bookshelf, Bed, Table, map_the_home, counter

class TestFurnishings(unittest.TestCase):
    
    def test_map_the_home(self):
        """
        Tests functionality of map_the_home function
        """
        self.home = [Bed('Bedroom'),
                     Sofa('Living Room'),
                     Table('Living Room'),
                     Bookshelf('Living Room'),
                     Table('Kitchen')]
        self.home_map = map_the_home(self.home)
        for item in self.home:
            self.assertTrue(item.room in self.home_map, 
                            "'{0}' is missing".format(item.room))
        
    
    def test_counter(self):
        """
        Tests the functionality of the counter function
        """
        self.home = [Bed('Bedroom'),
                     Sofa('Living Room'),
                     Table('Living Room'),
                     Bookshelf('Living Room'),
                     Table('Kitchen'),
                     Table('Patio'),
                     Bookshelf('Bedroom')]
        
        self.item_counts = counter(self.home)
        self.assertTrue(('Bookshelf', 2) in self.item_counts)
        self.assertTrue(('Bed', 1) in self.item_counts)
        self.assertTrue(('Sofa', 1) in self.item_counts)
        self.assertTrue(('Table', 3) in self.item_counts)
        
    
if __name__=="__main__":
    unittest.main()
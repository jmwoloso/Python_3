#!/usr/bin/python
#
# Test Suite For coconuts.py
#    test_coconuts.py
#
# Created by: Jason M Wolosonovich
#    6/02/2015
#
# Lesson 2 - Project Attempt 1
"""
test_coconuts.py: Test suite for coconuts.py

@author: Jason M. Wolosonovich
"""
import unittest
from coconuts import Coconut, Inventory

class TestCoconuts(unittest.TestCase):
    
    def test_weight(self):
        """
        Tests that different coconut types each have a different weight
        """
        # create a coconut of each type
        self.nuts = [Coconut(variety) for variety in ['middle eastern',
                                                      'south asian',
                                                      'american']]
        
        # check that weights are as expected
        self.weights = [2.5, 3.0, 3.5]
        for i in range(0,3):
            self.assertEqual(self.nuts[i]._Coconut__weight,
                             self.weights[i],
                             "The weight is wrong")
    
            
    def test_total_weight(self):
        """
        Tests that the sum of a specified number of coconuts of each type
        returned matches the expected total
        """
        varieties = [Coconut(variety) for variety in ['middle eastern',
                                                      'south asian',
                                                      'south asian',
                                                      'american',
                                                      'american',
                                                      'american']]
        self.inventory = Inventory()
        for variety in varieties:
            self.inventory.add_coconut(variety)
        self.assertEqual(self.inventory.total_weight(),
                         19.00,
                         "Your total weight is wrong")
        
            
    def test_string_attribute_errors(self):
        """
        Tests that a string passed as a coconut to the Inventory class
        throws an AttributeError
        """
        self.inventory = Inventory()
        with self.assertRaises(AttributeError):
            self.inventory.add_coconut('south asian')
 
    
if __name__=="__main__":
    unittest.main()
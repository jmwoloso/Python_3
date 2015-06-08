#!/usr/bin/python
#
# Test Suite For inhairitance.py
#    test_inhairitance.py
#
# Created by: Jason M Wolosonovich
#    6/02/2015
#
# Lesson 2 - Exercise 5
"""
test_inheritance.py: Inheritance test program

@author: Jason M. Wolosonovich
"""

import unittest
from inhairitance import Child

class TestHair(unittest.TestCase):
    
    def test_hair(self):
        """
        Test inheritance of hair color
        """
        child = Child()
        hair = child.hair()
        self.assertNotEqual(hair, "red")
        self.assertNotEqual(hair, "brown")
        self.assertNotEqual(hair, "gray")
        self.assertEqual(hair, "bald")
        
if __name__=="__main__":
    unittest.main()
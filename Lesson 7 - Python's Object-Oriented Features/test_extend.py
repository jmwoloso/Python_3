#!/usr/bin/python
#
# Test Suite For extend.py
#    test_extend.py
#
# Created by: Jason M Wolosonovich
#    6/04/2015
#
# Lesson 7 - Exercise 3
"""
test_extend.py: Test suite for extend.py; verify that Ford successfully 
                extends the Car.__init__() method

@author: Jason M. Wolosonovich
"""
import unittest
from extend import Car, Ford, Toyota

class TestCars(unittest.TestCase):
    
    def test_Toyota(self):
        car1 = Car("red", 2000)
        car2 = Toyota("red", 2000, "Corolla")
        self.assertEqual(car1.color, car2.color)
        self.assertEqual(car1.cc, car2.cc)
        self.assertEqual(car2.model, "Corolla")
        
    def test_Ford(self):
        car1 = Car("red", 2000)
        car2 = Ford("red", 2000, "Taurus")
        self.assertEqual(car1.color, car2.color)
        self.assertEqual(car1.cc, car2.cc)
        self.assertEqual(car2.model, "Taurus")
        
if __name__ == "__main__":
    unittest.main()
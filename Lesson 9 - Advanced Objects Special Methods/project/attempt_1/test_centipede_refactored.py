#!/usr/bin/python
#
# Test Suite For centipede.py
#    test_centipede_refactored.py
#
# Created by: Jason M Wolosonovich
# Reproduced by permission: O'Reilly School of Technology
#    6/05/2015
#
# Lesson 9 - Project Attempt 1
"""
test_centipede.py: Test suite for centipede.py

@author: Jason M. Wolosonovich
@author: Reproduced by permission: O'Reilly School of Technology
"""
import unittest
    
from centipede_refactored import Centipede

class TestBug(unittest.TestCase):
    def test_stomach(self):
        ralph = Centipede()
        ralph('chocolate')
        ralph('bbq')
        ralph('cookies')
        ralph('salad')
        self.assertEqual(ralph.__str__(), 'chocolate,bbq,cookies,salad')
        
    def test_legs(self):
        ralph = Centipede()
        ralph.friends = ['Steve', 'Daniel', 'Guido']
        ralph.favorite_show = "Monty Python's Flying Circus"
        ralph.age = '31'
        self.assertEqual(ralph.age, '31', "ralph doesn't know how old he is")
        self.assertEqual(ralph.__repr__(), 'friends,favorite_show,age')
        
        
    def test_protected(self):
        ralph = Centipede()
        self.assertRaises(AttributeError, setattr, ralph, "legs", [])
        self.assertRaises(AttributeError, setattr, ralph, "stomach", [])
        
    def test_EATstantiation(self):
        ralph = Centipede('pretzel', 'pickles')
        self.assertEqual(ralph.stomach, ['pretzel', 'pickles'])
        
    
if __name__ == "__main__":
    unittest.main()
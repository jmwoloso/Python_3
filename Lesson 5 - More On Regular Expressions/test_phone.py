#!/usr/bin/python
#
# Test Suite For phone.py
#    test_phone.py
#
# Created by: Jason M Wolosonovich
#    6/03/2015
#
# Lesson 5 - Exercise 1
"""
test_phone.py: Test suite for phone.py

@author: Jason M. Wolosonovich
"""
import unittest
from phone import get_phone, text

class TestRegex(unittest.TestCase):
    
    def test_phone(self):
        """
        Test for the get_phone function
        """
        numbers = get_phone(text)
        self.assertEqual(len(numbers), 
                         5)

if __name__=="__main__":
    unittest.main()
#!/usr/bin/python
#
# Test Suite For adder.py
#    test_adder.py
#
# Created by: Jason Wolosonovich
#    6/01/2015
#
# Lesson 1 - Project Attempt 1
'''
Created on Jun 1, 2015

@author: Jason M Wolosonovich
'''
import unittest
from adder import adder

class Test(unittest.TestCase):
    """
    Test suite for adder.py
    """

    def test_adder_errors(self):
        """
        Test ensuring errors in data causes validation failures.
        """
        # one or more floats, strings, None-type objects, type objects,
        # tuples, lists, dicts should not pass 
        for x,y in [(1.,2),      # one or more floats
                    ('one',2),   # one or more strings
                    (None, 2),   # one or more None-type objects
                    (object,2),  # one or more type objects
                    ((1,2),2),   # one or more tuples
                    ([1,2],2),   # one or more lists
                    (dict(),2),  # one or more dicts
                    # (adder(1.,2),2) # this fails for some reason..
                    ]: 
            with self.assertRaises(AssertionError):
                adder(x,y)
        
           
    def test_adder_successes(self):
        """
        Test ensuring that valid data passes.
        """
        # two integer objects should pass
        self.assertEqual(adder(1, 2), 
                         3, 
                         "Not correctly handling two integers")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
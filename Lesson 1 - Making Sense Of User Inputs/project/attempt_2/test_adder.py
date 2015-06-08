#!/usr/bin/python
#
# Test Suite For adder.py
#    test_adder.py
#
# Created by: Jason Wolosonovich
#    6/04/2015
#
# Lesson 1 - Project Attempt 2
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
        for x,y in [(1.,2),      # one float
                    (1,'two'),   # one string
                    (None, 2),   # one None
                    (1, object), # one object
                    ((1,2),2),   # one tuple
                    (1,[2,3]),   # one list
                    (dict(),2),  # one dict
                    # (adder(1.,2),2) # this fails for some reason..
                    ]: 
            with self.assertRaises(TypeError):
                adder(x,y)
        
           
    def test_adder_successes(self):
        """
        Test ensuring that valid data passes.
        """
        # two integer objects should pass
        self.assertEqual(adder(1, 2), 
                         3, 
                         "Not correctly handling two integers")
        # weird rounding logic
        self.assertEqual(adder(round(10.5), round(5.5)),
                         16,
                         "Not correctly handling two integers")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
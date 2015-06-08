#!/usr/bin/python
#
# Test Suite For ccn_safety2.py
#    test_ccn_safety2.py
#
# Created by: Jason M Wolosonovich
#    6/04/2015
#
# Lesson 6 - Project Attempt 1
"""
test_ccn_safety2.py: Test suite for ccn_safety2.py

@author: Jason M. Wolosonvich
"""
import unittest
from ccn_safety2 import ccn_safety2

text = """Have you ever noticed, in television and movies, that phone
numbers and credit cards are obviously fake numbers like 555-123-4567 or
5555-5555-5555-5555? It is because a number that appears to be real, such
as 1234-5678-1234-5678, triggers the attention of privacy and security
experts."""

class TestSafety(unittest.TestCase):
    
    def test_ccn_safety_successes(self):
        """
        Tests ccn_safety function
        """
        response, count = ccn_safety2(text)
        self.assertFalse("5555-5555-5555-5555" in response)
        self.assertTrue("CCN REMOVED FOR YOUR SAFETY" in response)
        self.assertEqual(2,
                         count)
    
    def test_ccn_safety_failures(self):
        """
        Tests that ccn_safety is not inadvertently substituting numbers
        when it shouldn't be
        """
        response, _  = ccn_safety2(text)
        # make sure it doesn't obscure phone numbers
        self.assertFalse("XXX-XXX-44567" in response)
        
    
if __name__=="__main__":
    unittest.main()
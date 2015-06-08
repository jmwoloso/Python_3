#!/usr/bin/python
#
# Test Suite For ccn_safety.py
#    test_ccn_safety.py
#
# Created by: Jason M Wolosonovich
#    6/03/2015
#
# Lesson 5 - Project Attempt 1
"""
test_ccn_safety.py: Test suite for ccn_safety.py

@author: Jason M. Wolosonvich
"""
import unittest
from ccn_safety import ccn_safety

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
        response, count = ccn_safety(text)
        self.assertFalse("5555-5555-5555-5555" in response)
        self.assertTrue("XXXX-XXXX-XXXX-5555" in response)
        self.assertTrue("XXXX-XXXX-XXXX-5678" in response)
        self.assertEqual(2,
                         count)
    
    def test_ccn_safety_failures(self):
        """
        Tests that ccn_safety is not inadvertently substituting numbers
        when it shouldn't be
        """
        response, _  = ccn_safety(text)
        # make sure it doesn't obscure phone numbers
        self.assertFalse("XXX-XXX-44567" in response)
        
    
if __name__=="__main__":
    unittest.main()
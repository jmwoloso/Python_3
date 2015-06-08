#!/usr/bin/python
#
# Test Suite For find_regex.py
#    test_find_regex.py
#
# Created by: Jason M Wolosonovich
#    6/03/2015
#
# Lesson 4 - Project Attempt 1
"""
test_find_regex.py: Test suite for find_regex.py

@author: Jason M. Wolosonovich
"""
import unittest
from find_regex import find_regex

# text to send to find_regex
text=\
"""In the 1950s, mathematician Stephen Cole Kleene described automata
theory and formal language theory in a set of models using a
notation called "regular sets" as a method to do pattern matching.
Active usage of this system, called Regular Expressions, started in
the 1960s and continued under such pioneers as David J. Farber,
Ralph E. Griswold, Ivan P. Polonsky, Ken Thompson, and Henry
Spencer."""


class TestFindRegex(unittest.TestCase):
    """
    Test suit for find_regex.py
    """
    def test_find_regex_successes(self):
        """
        Tests that find_regex is functioniong correctly
        """
        self.assertEqual(find_regex("Regular Expressions",
                                    text),
                         (231, 250),
                         "Search is incorrectly failing.")
        
    
    def test_find_regex_errors(self):
        """
        Test that find_regex is not returning unacceptable strings
        """
        self.assertIsNone(find_regex("I remember you painting "+\
                                     "sunflowers in your room.",
                                     text),
                          "Test should not be returning anything.")
        
    
if __name__=="__main__":
    unittest.main()
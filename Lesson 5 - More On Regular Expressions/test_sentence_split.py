#!/usr/bin/python
#
# Test Suite For sentence_split.py
#    test_sentence_split.py
#
# Created by: Jason M Wolosonovich
#    6/03/2015
#
# Lesson 5 - Exercise 9
"""
test_sentence_split.py: Test suite for sentence_split.py

@author: Jason M. Wolosonovich
"""
import unittest
from sentence_split import sentence_split

text = """Hello! My name is Steve. What is yours? I hope you enjoyed this
class!"""

class TestRegex(unittest.TestCase):
    
    def test_sentence_split(self):
        numbers = sentence_split(text)
        self.assertEqual(len(numbers),
                         4)

if __name__=="__main__":
    unittest.main()
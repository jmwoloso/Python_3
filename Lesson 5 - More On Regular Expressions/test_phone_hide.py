#!/usr/bin/python
#
# Test Suite For phone_hide.py
#    test_phone_hide.py
#
# Created by: Jason M Wolosonovich
#    6/03/2015
#
# Lesson 5 - Exercise 7
"""
test_phone_hide.py: Test suite for phone_hide.py

@author: Jason M. Wolosonovich
"""
import unittest
from phone_hide import phone_hide

text= """While I was at the store I tried to call 555-123-4567 on my
mobile but accidentally called 555-754-4321.  The person on the line
redirected me to 999-999-9999 which I don't think is a real number.
Neither is 000-000-0000 or 555-555-0000. Well, I will try
(555)-123-4567 again now."""

class TestRegex(unittest.TestCase):
    
    def test_phone(self):
        response, count = phone_hide(text)
        self.assertFalse("555-123-4567" in response)
        self.assertTrue("555-XXX-XXXX" in response)
        self.assertTrue("(555)-XXX-XXXX" in response)
        self.assertEqual(6, count)

if __name__=="__main__":
    unittest.main()        
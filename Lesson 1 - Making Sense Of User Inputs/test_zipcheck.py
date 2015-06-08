#!/usr/bin/python
#
# Test Suite For Command-Line Zip Code Validation
#    test_zipcheck.py
#
# Created by: Jason Wolosonovich
#    6/01/2015
#
# Lesson 1 - Exercise 2
'''
Created on Jun 1, 2015

@author: Jason M Wolosonovich

Test the zip_errors() function from the zipcheck module
'''
import unittest
from zipcheck import zip_errors

class Test(unittest.TestCase):
    """
    Test suite for zipcheck.py
    """

    def test_zip_errors(self):
        """
        Tests ensuring errors in the data cause validation failures.
        """
        # 4-digit zips should be rejected
        self.assertIsNotNone(zip_errors("1234"), 
                             "Accepting length 4")
        # 8-digit zips should be rejected
        self.assertIsNotNone(zip_errors("12345-678"), 
                             "Accepting length 9")
        # alphabetic characters should be rejected for 5-digit zips
        self.assertIsNotNone(zip_errors("1234e"), 
                             "Accepting alphabetic 5")
        # alphabetic characters should be rejected for 10-digit zips
        self.assertIsNotNone(zip_errors("12345-678Y"), 
                             "Accepting alphabetic 5+4")
        # 9-digit zips should be hyphenated only
        self.assertIsNotNone(zip_errors("12345/6789"), 
                             "Accepting non-hyphen")    
    
    
    def test_zip_successes(self):
        """
        Test ensuring that valid data passes.
        """
        # 5-digit zips should be accepted
        self.assertIsNone(zip_errors("12345"), 
                          "Not accepting 5-digit zips")
        # 9-digit zips should be accepted
        self.assertIsNone(zip_errors("12345-6789"), 
                          "Not accepting 9-digit zips")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_zip_errors']
    unittest.main()
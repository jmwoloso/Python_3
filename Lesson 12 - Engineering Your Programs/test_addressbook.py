#!/usr/bin/python
#
# Test Suite For addressbook.py
#    test_addressbook.py
#
# Created by: Jason M Wolosonovich
#    6/10/2015
#
# Lesson 12 - Exercise 2
"""
test_addressbook.py: Test suite for addressbook.py

@author: Jason M. Wolosonovich
"""
import unittest, shelve
import addressbook

class TestEmailHandlers(unittest.TestCase):
    
    def setUp(self):
        self.email = 'test123@t.com'
        shelf_location = addressbook.shelf_location
        
        shelf = shelve.open(shelf_location)
        if 'emails' in shelf:
            if self.email in shelf['emails']:
                shelf['emails'] = []
        shelf.close()
        
    def test_email_delete(self):
        # ensure the email is active
        addressbook.email_add(self.email)
        self.assertEqual(addressbook.email_delete(self.email)[0], True)
        self.assertEqual(addressbook.email_delete(self.email)[0], False)
        
    def test_email_add(self):
        self.assertEqual(addressbook.email_add(self.email)[0], True)
        self.assertEqual(addressbook.email_add(self.email)[0], False)
        
    def test_email_display(self):
        addressbook.email_add(self.email)
        val, display = addressbook.email_display()
        self.assertTrue(self.email in display)
        
if __name__=="__main__":
    unittest.main()
#!/usr/bin/python
#
# Test Suite For property_address.py
#    test_property_address.py
#
# Created by: Jason M Wolosonovich
# Reproduced by permission: O'Reilly School of Technology
#    6/08/2015
#
# Lesson 10 - Project Attempt 1
"""
test_property_address.py: Test suite for property_address.py

@author: Jason M. Wolosonovich
@author: Reproduced by permission: O'Reilly School of Technology
"""
import unittest
from property_address import *
 
class TestAddresses(unittest.TestCase): 
   
    def setUp(self): 
        self.home = Address( name='Steve Holden', street_address='1972 Flying Circus', city='Arlington', state='VA', zip_code='12345' )
        self.home2 = Address( name=' steve holdeN ', street_address=' 1972 flying circus  ', city=' arlington  ', state='VA', zip_code='12345' )       
    
    
    def test_name(self): 
        self.assertEqual(self.home.name, 'Steve Holden') 
        self.assertRaises(AttributeError, setattr, self.home, 'name', 'Daniel Greenfeld')
        
    
    def test_formatting(self):
        # test formatting
        self.assertEqual(self.home2.name, 'Steve Holden')
        self.assertEqual(self.home2.street_address, '1972 Flying Circus')
        self.assertEqual(self.home2.city, 'Arlington')
        
        
    def test_setattr(self):
        # test that attributes that allow replacement function correctly
        self.home.street_address = '1972 E. Broadway Rd.'
        self.assertEqual(self.home.street_address, '1972 E. Broadway Rd.')
        self.home.city = 'Tempe'
        self.assertEqual(self.home.city, 'Tempe')
        self.home.state = 'AZ'
        self.assertEqual(self.home.state, 'AZ')
        self.home.zip_code = '85282'
        self.assertEqual(self.home.zip_code, '85282')
        
          
    def test_state(self): 
        self.assertEqual(self.home.state, 'VA') 
        self.assertRaises(StateError, setattr, self.home, 'state', 'Not a state')  
        self.home.state = 'CO' 
        self.assertEqual(self.home.state, 'CO') 
        # check for correct state length
        self.assertRaises(StateError, setattr, self.home, 'state', 'AZZ')
        
    def test_zip_code(self): 
        self.assertEqual(self.home.zip_code, '12345') 
        self.assertRaises(ZipCodeError, setattr, self.home, 'zip_code', '123456')   
        self.home.zip_code = '54321' 
        self.assertEqual(self.home.zip_code, '54321') 
       
if __name__ == "__main__": 
    unittest.main() 
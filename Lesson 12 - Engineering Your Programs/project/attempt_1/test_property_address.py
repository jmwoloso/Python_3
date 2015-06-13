#!/usr/bin/python
#
# Test Suite For property_address.py
#    test_property_address.py
#
# Created by: Jason M Wolosonovich
# Reproduced by permission: O'Reilly School of Technology
#    6/11/2015
#
# Lesson 12 - Project Attempt 1
"""
test_property_address.py: Test suite for property_address.py
                          incuding logging

@author: Jason M. Wolosonovich
@author: Reproduced by permission: O'Reilly School of Technology
"""
import unittest
from property_address import *
 
class TestAddresses(unittest.TestCase): 
   
    def setUp(self): 
        self.home = Address( name='Steve Holden', street_address='1972 Flying Circus', city='Arlington', state="VAA", zip_code="12345-6789" )
            
    
    def test_name(self): 
        self.assertEqual(self.home.name, 'Steve Holden') 
        self.assertRaises(NameError, setattr, self.home, 'name', 'Daniel Greenfeld')
        
        
    def test_state(self): 
        self.assertEqual(self.home.state, 'VAA') 
        self.assertRaises(StateError, setattr, self.home, 'state', 'Not a state')  
        self.home.state = 'COO' 
        self.assertEqual(self.home.state, 'COO') 
        
        
    def test_zip_code(self): 
        self.assertEqual(self.home.zip_code, '12345-6789') 
        self.assertRaises(ZipCodeError, setattr, self.home, 'zip_code', '12345')   
        self.home.zip_code = '54321-9876' 
        self.assertEqual(self.home.zip_code, '54321-9876') 
       
if __name__ == "__main__":
    # begin logging
    start_logging(level='info') 
    unittest.main() 
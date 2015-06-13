#!/usr/bin/python
#
# Program To Demonstrate Properties Using Property Addresses And Logging
#    property_address.py
#
# Created by: Jason M Wolosonovich
#    6/09/2015
#
# Lesson 11 - Project Attempt 1
"""
property_address.py: Demonstrates properties using property addresses
                     and logging

@author: Jason M. Wolosonovich
"""
import re
import logging


# setup logging functionality
LOG_FILENAME = "property_address.log"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
DEFAULT_LOG_LEVEL = 'debug'
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
          }


def start_logging(filename=LOG_FILENAME, level=DEFAULT_LOG_LEVEL, fmt=None):
    """
    Starts logging when called. Can be called with alternate arguments
    for 'filename', 'level' and 'fmt' (format).
    """
    # configure logging
    logging.basicConfig(filename=filename, level=LEVELS[level], format=LOG_FORMAT)
    # startup message
    logging.info("BEGIN LOGGING PROPERTY_ADDRESS.PY")
    
    
    
# create StateError exception
class StateError(Exception):
    """
    Custom StateError exception.
    """
    def __init__(self, arg):
        msg = "STATE exception"
        logging.error(msg)
        self.msg = arg
            
# create ZipCodeError exception
class ZipCodeError(Exception):
    """
    Custom ZipCodeError exception
    """
    def __init__(self, arg):
        msg = "ZIPCODE exception"
        logging.error(msg)
        self.msg = arg
    
        
    
class Address(object):
    """
    Address class for storing property information
    """
    def __init__(self, name, street_address, city, state, zip_code):
        msg = "Creating a new address"
        logging.info(msg)
        self._name = name # internal attribute
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        
        
    
    # name properties
    @property
    def name(self):
        # self._name can still be set!!
        # self.name cannot be set though
        return self._name.strip().title()
    
      
    @property
    def street_address(self):
        # use string methods to return title case formatting
        return self._street_address
    
    @street_address.setter
    def street_address(self, value):
        # for fun let's format the address with title case
        
        addy_list = re.split(' ', 
                             value.strip() )
        # put address back together in title case
        addy_list = [part.title() for part in addy_list]
        street_address = " ".join(addy_list)
        self._street_address = street_address
        
    @street_address.deleter
    def street_address(self):
        del self._street_address
    
    
    # city properties
    @property
    def city(self):
        # return title case string
        return self._city.title()
    
    @city.setter
    def city(self, value):
        value = value.strip()
        value = value.title()
        self._city = value
    
    @city.deleter
    def city(self):
        del self._city
    
    
    # state properties
    @property
    def state(self):
        """
        Getter for self._state attribute.
        """
        return self._state
    
    @state.setter
    def state(self, value):
        """
        Setter for self._state attribute. State argument must be entered
        in all capital letters.
        
        e.g. state='AZ'
        """
        # find two consecutive capital letters
        regex = r"^[A-Z]{2}$"
        state = re.search(regex,
                          value)
        if not state:
            raise StateError("StateError: 'state' argument must have two capital letters")
        else:
            self._state = value
    
    @state.deleter
    def state(self):
        del self._state
    
    
    # zip code properties
    @property
    def zip_code(self):
        return self._zip_code
    
    @zip_code.setter
    def zip_code(self, value):
        """
        Setter for self._zip_code. Zip code argument must be entered as
        a 5-digit (U.S.-style) code with integers only.
        """
        regex = r"^\d{5}$"
        zipcode = re.findall(regex,
                            value)
        if not zipcode:
            raise ZipCodeError("ZipCodeError: 'zip_code' must be 5 non-float digits")
        else:
            self._zip_code = value
            
    @zip_code.deleter
    def zip_code(self):
        del self._zip_code
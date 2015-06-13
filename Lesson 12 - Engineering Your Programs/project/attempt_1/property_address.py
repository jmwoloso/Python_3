#!/usr/bin/python
#
# Program To Demonstrate Properties Using Property Addresses And Logging
#    property_address.py
#
# Created by: Jason M Wolosonovich
#    6/11/2015
#
# Lesson 12 - Project Attempt 1
"""
property_address.py: Demonstrates properties using property addresses
                     and logging

@author: Jason M. Wolosonovich
"""
import re
import logging
import configparser
from optparse import OptionParser, make_option


# configparser setup
config = configparser.RawConfigParser()
config.read('property_address.cfg')


# setup logging functionality
LOG_FILENAME = config.get('log', 'output')
LOG_FORMAT = config.get('log', 'format')
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
    logging.basicConfig(filename=filename, level=LEVELS[level.lower()], format=LOG_FORMAT)
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
        
class NameError(Exception):
    """
    Custom NameError exception
    """
    def __init__(self, arg):
        msg = "NAME exception"
        logging.error(msg)
        self.msg = msg
    
        
    
class Address(object):
    """
    Address class for storing property information
    """
    def __init__(self, name, street_address, city, state, zip_code):
        msg = "Creating a new address"
        logging.info(msg)
        self._name = name
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        
       
    # name properties
    @property
    def name(self):
        return self._name.strip().title()
    
    @name.setter
    def name(self, name):     
        if name:
            raise NameError("'Name' can only be set once for an instance")
    
      
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
        regex = config.get('validators', 'state')
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
        regex = config.get('validators', 'zip_code')
        zipcode = re.search(regex,
                            value)
        if not zipcode:
            raise ZipCodeError("ZipCodeError: 'zip_code' must be 5 non-float digits")
        else:
            self._zip_code = value
            
    @zip_code.deleter
    def zip_code(self):
        del self._zip_code


def main(options):        
    """
    Main loop for property_address.py. Takes the CLI options and
    arguments and runs the program.
    """
    home = Address(options.name,
                   options.address,
                   options.city,
                   options.state,
                   options.zip_code)
    
    
if __name__=="__main__":
    # setup for command line parsing
    # create option list to send to parser
    option_list = [
                   # level option
                   make_option("-l", 
                               "--loglevel", 
                               action="store", 
                               dest="level", 
                               default="info",
                               help="set level of logger:"+\
                                    " debug, info, warning (default),"+\
                                    " error, critical"),
                   # name option
                   make_option("-n", 
                               "--name", 
                               action="store", 
                               dest="name", 
                               help="name of resident"),
                   # address option
                   make_option("-a", 
                               "--address", 
                               action="store", 
                               dest="address", 
                               help="address of residence"),
                   # city option
                   make_option("-c", 
                               "--city", 
                               action="store", 
                               dest="city", 
                               help="city of residence"),
                   # state option
                   make_option("-s", 
                               "--state", 
                               action="store", 
                               dest="state", 
                               help="state of residence"),
                   # zip_code option
                   make_option("-z", 
                               "--zip_code", 
                               action="store", 
                               dest="zip_code", 
                               help="zip code of residence"),
                  ]
    # instantiate parser
    parser = OptionParser(option_list=option_list)
    # get stored options,args
    (options, args) = parser.parse_args()
        
    # validate options,args
    errors = []
    if not options.name:
        errors.append("-n")
    if not options.address:
        errors.append("-a")
    if not options.city:
        errors.append("-c")
    if not options.state:
        errors.append("-s")
    if not options.zip_code:
        errors.append("-z")
    if len(errors) > 0:
        if len(errors) == 1:
            parser.error("{0} is required".format("".join(errors)))
        else:
            parser.error("{0} are required".format(", ".join(errors)))
    
    try:
        # process input and run program
        start_logging(level=options.level)
        main(options)
    except StateError:
        parser.error("-s requires a valid, capitalized US state abbreviation")
    except ZipCodeError:
        parser.error("-z requires a valid 5-digit US zip code")
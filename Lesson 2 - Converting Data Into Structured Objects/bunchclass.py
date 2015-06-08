#!/usr/bin/python
#
# Program To Demonstrate Bunch Classes
#    bunchclass.py
#
# Created by: Jason Wolosonovich
#    6/02/2015
#
# Lesson 2 - Exercise 1
"""
bunchclass.py: Demonstrating the creation of a bunch class with a pretty
               printing method and API protection

@author: Jason M. Wolosonovich
"""
import unittest


class Bunch(object):
    def __init__(self, **kwargs):
        """
        Instantiation directions for Bunch class
        """
        for key, value in kwargs.items():
            if hasattr(self, 
                       key):
                raise AttributeError("API conflict: "\
                                     "{0} is part of the {1} API"\
                                     .format(key, 
                                             self.__class__.__name__))
            else:
                setattr(self, 
                        key, 
                        value)
        
    def pretty(self):
        """
        Pretty-print method for Bunch class
        """
        text = ""
        for key, value in self.__dict__.items():
            text += "{0}: {1}\n".format(key, 
                                        value)
        return text


class TestBunch(unittest.TestCase):        
        """
        Test suite for bunchclass.py
        """        
        def test_pretty(self):
            """
            Testing pretty method of Bunch class
            """
            self.assertRaises(AttributeError,
                              Bunch,
                              name="Audrey",
                              job="Software Developer",
                              pretty=True)
            b = Bunch(name="Audrey",
                      job="Software Developer")
            p = b.pretty()
            self.assertTrue("Audrey" in p)
            self.assertFalse("pretty: True" in p)

if __name__=="__main__":
    unittest.main()
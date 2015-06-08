#!/usr/bin/python
#
# Program To Demonstrate Magic Methods For Attribute Access
#    attrmagic.py
#
# Created by: Jason M Wolosonovich
#    6/05/2015
#
# Lesson 9 - Exercise 4
"""
attrmagic.py: Demonstrates magic methods for attribute access

@author: Jason M. Wolosonovich
"""

class AttrMixin:
    """
    Displays a message when an instance's attributes are retrieved,
    deleted or set
    """
    def __setattr__(self, key, value):
        print("ATTR: setting attribute {0!r} to {1!r}".format(key,
                                                              value))
        self.__dict__[key] = value
        
    def __getattr__(self, key):
        print("ATTR: getting attribute {0!r}".format(key))
        # searches for the attribute first then sets it if not found
        self.__getattr__(key, "No value")
        return "No value"
    
    def __delattr__(self, key):
        print("ATTR: Deleting key {0!r}".format(key))
        object.__delattr__(self, key)
        
        
class Person(AttrMixin):
    """
    Represents a person
    """
    def __init__(self, name):
        self.name = name
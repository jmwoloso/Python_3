#!/usr/bin/python
#
# Program To Demonstrate __new__() Magic Method
#    newmagic.py
#
# Created by: Jason M Wolosonovich
#    6/05/2015
#
# Lesson 9 - Exercise 1
"""
newmagic.py: Python classes with magic methods

@author: Jason M. Wolosonovich
"""

class ustr(str):
    """
    An uppercase string object
    """
    def __new__(cls, arg):
        arg = str(arg)
        return str.__new__(cls, arg.upper())
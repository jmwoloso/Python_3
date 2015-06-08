#!/usr/bin/python
#
# Program To Take Two Objects And Add Them Together
#    adder.py
#
# Created by: Jason Wolosonovich
#    6/04/2015
#
# Lesson 1 - Project Attempt 2
"""
adder.py: takes two objects and adds them together only if they are
          both an integer type.

@author: Jason M Wolosonovich
"""

def adder(x=None, y=None):
    """
    Function to add two integers together.
    """
    if not isinstance(x, int):
        raise TypeError("'x' must be of type <int>")
    
    if not isinstance(y, int):
        raise TypeError("'y' must be of type <int>")
    
    return x + y
        
    
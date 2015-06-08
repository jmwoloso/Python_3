#!/usr/bin/python
#
# Program To Take Two Objects And Add Them Together
#    adder.py
#
# Created by: Jason Wolosonovich
#    6/01/2015
#
# Lesson 1 - Project Attempt 1
"""
adder.py: takes two objects and adds them together only if they are
          both an integer type.

@author: Jason M Wolosonovich
"""

def adder(x=None, y=None):
    """
    Function to add two integers together.
    """
    assert type(x) is int, "Values must be of type <int>"
    assert type(y) is int, "Values must be of type <int>"
    return x + y
        
    
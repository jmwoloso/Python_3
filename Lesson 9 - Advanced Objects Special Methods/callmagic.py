#!/usr/bin/python
#
# Program To Demonstrate Making Instances Callable
#    callmagic.py
#
# Created by: Jason M Wolosonovich
#    6/05/2015
#
# Lesson 9 - Exercise 5
"""
callmagic.py: Demonstrates how to make instances callable

@author: Jason M. Wolosonovich
"""

class funclike:
    def __call__(self, *args, **kwargs):
        print("Args are: ", args)
        print("Kwargs are: ", kwargs)
        
f = funclike()
f(1, 2, 3, this="one", that="the other")
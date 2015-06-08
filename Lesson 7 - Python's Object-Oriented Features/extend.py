#!/usr/bin/python
#
# Program To Demonstrate Extending Classes With Superclass Method
#    extend.py
#
# Created by: Jason M Wolosonovich
#    6/04/2015
#
# Lesson 7 - Exercise 4
"""
extend.py: Demonstrates how to extend a superclass method

@author: Jason M. Wolosonovich
"""

class Car:
    
    def __init__(self, color, cc):
        self.color = color
        self.cc = cc
        
class Toyota(Car):
    
    def __init__(self, color, cc, model):
        Car.__init__(self, color, cc)
        self.model = model
        
class Ford(Car):
    
    def __init__(self, color, cc, model):
        super().__init__(color, cc)
        self.model = model
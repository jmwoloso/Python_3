#!/usr/bin/python
#
# Program To Demonstrate String Representations Using Inheritance
#    strmagic.py
#
# Created by: Jason M Wolosonovich
#    6/05/2015
#
# Lesson 9 - Exercise 2
"""
strmagic.py: Demonstrates string representations using inheritance

@author: Jason M. Wolosonovich
"""

class Person:
    """
    Represents a person
    """
    def __init__(self, name):
        self.name = name
    
class NamedPerson(Person):
    """
    Represents a person using their name
    """
    def __str__(self):
        return self.name
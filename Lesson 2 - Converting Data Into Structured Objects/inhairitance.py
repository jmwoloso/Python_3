#!/usr/bin/python
#
# Program To Demonstrate Class Inheritance
#    inhairitance.py
#
# Created by: Jason Wolosonovich
#    6/02/2015
#
# Lesson 2 - Exercise 4
"""
inhairitance.py: Complex inheritance program

@author: Jason M. Wolosonovich
"""

import unittest

class Maurice(object):
    """
    Grandpa Maurice
    """
    def hair(self):
        return "red"
    
class Vivian(object):
    """
    Grandma Vivian
    """
    def hair(self):
        return "brown"
    
class Isadore(object):
    """
    Grandpa Isadore
    """
    def hair(self):
        return "bald"

class Tracy(object):
    """
    Grandma Tracy
    """
    def hair(self):
        return "gray"
    
class Mother(Maurice, Vivian):
    pass

class Father(Isadore, Tracy):
    pass

class Child(Father, Mother):
    pass

if __name__=="__main__":
    child = Child()
    print(child.hair())
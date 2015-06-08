#!/usr/bin/python
#
# Program To Demonstrate Class Polymorphism
#    animal_farm.py
#
# Created by: Jason M Wolosonovich
#    6/04/2015
#
# Lesson 7 - Exercise 2
"""
animal_farm.py: Demonstrates class polymorphism

@author: Jason M. Wolosonovich
"""

class Animal(object):
    
    def __init__(self, name):
        self.name = name
        
    def sound(self):
        raise NotImplementedError("Animals need a sound method")
    
    def has_wings(self):
        return False
    
class Pig(Animal):
    
    def sound(self):
        return "oink!"
    
class Dog(Animal):
    
    def sound(self):
        return "woof!"
    
class Chicken(Animal):
    
    def sound(self):
        return "bok bok!"
    
    def has_wings(self):
        return True
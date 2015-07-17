#!/usr/bin/python
#
# Program To Perform Computations On Instance Attributes
#    teacher_simple.py
#
# Created by: Jason M. Wolosonovich
#    6/08/2015
#
# Lesson 10 - Exercise 1
"""
teacher_simple.py: Demonstrates performing computations on stored attributes
                   via the __getattr__ magic.

@author: Jason M. Wolosonovich
"""

class Teacher(object):
    
    grades = {1: "First",
              2: "Second",
              3: "Third",
              4: "Fourth",
              5: "Fifth"
              }
    
    def __init__(self, first_name, last_name, age, classes, grade):
        # this ensures normal attribute lookup fails and that
        # our __getattr__ method will be called below
        self.__dict__['_attrs'] = {}
        # create remaining attributes as normal
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.classes = classes
        self.grade = grade
        
    def __setattr__(self, name, value):
        self._attrs[name] = value
        
    def __getattr__(self, name):
        # normal attribute lookup failed (intentionally)
        # and now we can ensure the attributes are returned
        # in the proper format that we want
        if name not in self._attrs:
            raise AttributeError("Teacher has no attribute {0!r}"\
                                 .format(name))
        value = self._attrs[name]
        if name in ("first_name", "last_name"):
            return value.capitalize()
        elif name == "age":
            return int(value)
        elif name == "classes":
            return sorted(value)
        elif name == "grade":
            return self.grades[value]
        else:
            return value
    
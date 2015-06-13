#!/usr/bin/python
#
# Program To Perform Computations On Instance Attributes
#    teacher.py
#
# Created by: Jason M. Wolosonovich
#    6/08/2015
#
# Lesson 10 - Exercise 1
"""
teacher.py: Demonstrates performing computations on managed attributes
            via properties

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
        # set internal (managed) attribures
        self._first_name = first_name
        self._last_name = last_name
        self.age = age
        self._classes = classes
        self._grade = grade
    
    # apply decorators
    @property    
    def first_name(self):
        return self._first_name.capitalize()
    #alternate below if not using @property
    #first_name = property(first_name)
    
    @property
    def last_name(self):
        return self._last_name.capitalize()
    #last_name = property(last_name)
    
    @property
    def age(self):
        return int(self._age)
    
    @age.setter
    def age(self, value):
        self._age = int(value)
        
    @property
    def classes(self):
        return sorted(self._classes)
    #classes = property(classes)
    
    @property
    def grade(self):
        return self.grades[self._grade]
    #grade = property(grade)
    
    @grade.setter
    def grade(self, value):
        # throws an error if value is not a key
        self.grades[value]
        self._grade = value
        
    @grade.deleter
    def grade(self):
        self.age += 1
        del self._grade
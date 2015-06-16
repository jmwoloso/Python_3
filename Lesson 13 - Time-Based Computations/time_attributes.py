#!/usr/bin/python
#
# Program To Demonstrate Retrieving Time Attributes
#    time_attributes.py
#
# Created by: Jason M Wolosonovich
#    6/11/2015
#
# Lesson 13 - Exercise 7
"""
time_attributes.py: Demonstrates how to retrieve time attributes
                    from datetime objects.
                    
@author: Jason M. Wolosonovich
"""
from datetime import datetime
dt = datetime(2012, 10, 31, 12, 30, 59, 300)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)
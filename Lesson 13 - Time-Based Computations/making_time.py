#!/usr/bin/python
#
# Program To Make Different Time Specificities
#    making_time.py
#
# Created by: Jason M Wolosonovich
#    6/11/2015
#
# Lesson 13 - Exercise 6
"""
making_time.py: Demonstrates making times with different levels of
                specificity.
                
@author: Jason M. Wolosonovich
"""
from datetime import datetime
print(datetime(2012, 10, 31))
print(datetime(2012, 10, 31, 12))
print(datetime(2012, 10, 31, 12, 30))
print(datetime(2012, 10, 31, 12, 30, 59))
print(datetime(2012, 10, 31, 12, 30, 59, 300))
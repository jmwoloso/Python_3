#!/usr/bin/python
#
# Program To Demonstrate The Complexity Of Counting Days From A Point In Time
#    count_thirtyone_days.py
#
# Created by: Jason M Wolosonovich
#    6/11/2015
#
# Lesson 13 - Exercise 1
"""
count_thirtyone_days.py: Demonstrates the complexity of measuring time,
                         in days, from a point in time
                         
@author: Jason M. Wolosonovich
"""
from datetime import datetime, timedelta

now = datetime.now()
# timedelta of 31 days
delta = timedelta(31)
delivery = now + delta
print("Today: %s" % now.strftime("%d"))
print("Delivery: %s" % delivery.strftime("%d"))
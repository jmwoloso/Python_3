#!/usr/bin/python
#
# Program To Demonstrate Skipping Over Weekends
#    skip_weekends.py
#
# Created by: Jason M Wolosonovich
#    6/11/2015
#
# Lesson 13 - Exercise 2
"""
skip_weekends.py: Demonstrates skipping over weekends in time calcs

@author: Jason M. Wolosonovich
"""
from datetime import datetime, timedelta

delivery = datetime.now()
delta = timedelta(1)
count = 0
while count < 31:
    delivery = delivery + delta
    if delivery.isoweekday() in (6,7):
        continue
    count += 1
    
now = datetime.now()
print(now)
print(delivery)
print("Today: %s" % now.strftime("%d"))
#!/usr/bin/python
#
# Program To Demonstrate Construction Of Various Timedeltas
#    more_deltas.py
#
# Created by: Jason M Wolosonovich
#    6/11/2015
#
# Lesson 13 - Exercise 3
"""
more_deltas.py: Demonstrates how to construct timedeltas of varous lengths

@author: Jason M. Wolosonovich
"""
from datetime import datetime, timedelta

weeks = timedelta(weeks=2)
hours = timedelta(hours=1)
minutes = timedelta(minutes=100)
seconds = timedelta(seconds=1000)
composite = timedelta(hours=1, minutes=30)

now = datetime.now()
print(now)
print(now + weeks)
print(now + hours)
print(now + minutes)
print(now + seconds)
print(now + composite)
#!/usr/bin/python
#
# Program To Generate Sequences From A Base List
#    gen123.py
#
# Created by: Jason Wolosonovich
#    6/02/2015
#
# Lesson 3 - Exercise 3
"""
gen123.py: generate sequences from a base list, repeating each element
           one more time than the last

@author: Jason M. Wolosonovich
"""

def gen123(m):
    n = 0
    for item in m:
        n += 1
        for i in range(n):
            yield item
#!/usr/bin/python
#
# Program Demonstrating Custom Fixed-Length Sequence With Old Protocol
#    fls.py
#
# Created by: Jason Wolosonovich
#    6/02/2015
#
# Lesson 3 - Exercise 1
"""
fls.py: Simple demonstration of the "old iteration protocol" - still available.

@author: Jason M. Wolosonovich
"""

class fls(object):
    def __init__(self, val, times):
        self.val = val
        self.count = times
        
    def __getitem__(self, n):
        if n >= self.count:
            raise IndexError("Object has no item {0}".format(n, ))
        return self.val

thing = fls("*", 5)
for c in thing:
    print(c)
    
thing = fls(120,3)
for c in thing:
    print(c)
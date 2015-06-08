#!/usr/bin/python
#
# Program Demonstrating Match Vs. Search From re Module
#    match_vs_search.py
#
# Created by: Jason M Wolosonovich
#    6/03/2015
#
# Lesson 5 - Exercise 4
"""
match_vs_search.py: Demonstrates the difference between match()
                    and search() in the re module.
                    
@author: Jason M. Wolosonovich
"""

import re

def check_number(text):
    regex = r"(\d\d\d|\(\d\d\d\))(-| )\d\d\d-\d\d\d\d"
    match = re.match(regex,
                     text)
    if match:
        return match.group()
    match = re.search(regex,
                      text)
    if match:
        return len(text)
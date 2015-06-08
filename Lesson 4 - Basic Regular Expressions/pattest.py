#!/usr/bin/python
#
# Program To Test Out Regex Patterns
#    pattest.py
#
# Created by: Jason Wolosonovich
#    6/03/2015
#
# Lesson 4 - Exercise 1
"""
pattest.py: Allows the checking of various patterns and target strings

@author: Jason M. Wolosonovich

Try these patterns:

[0123456789]+   # Matches one or more decimal digits. 
[\d]+           # Same as above. Remember to verify that some strings
                # don't match the pattern - 
[\w]+ +[\w]+    # Matches two words separated by any number of spaces. 
\(\d\d\d\) \d\d\d-\d\d\d\d  # Matches a US telephone number with 
                            # parentheses around the area code and a 
                            # dash between the exchange and the number. 
home-?brew      # There should be exactly two strings that match this 
                # pattern. 
\$\d+(\.\d{2})? # An amount of money (in dollars) with optional cents. 

"""
import re

while True:
    pat = input("Pattern: ")
    if not pat:
        break
    while True:
        s = input("Target: ")
        if not s:
            break
        mm = re.match(pat,
                      s)
        if mm:
            print("Match : matched {0!r}".format(s[mm.start():mm.end()]))
            print("Match: groups:", mm.groups())
            print("Match: gdict :", mm.groupdict())
        else:
            print("Match : no match")
        ms = re.search(pat,
                       s)
        if ms:
            print("Search: matched {0!r}".format(s[ms.start():ms.end()]))
            print("Search: groups:", ms.groups())        
            print("Search: gdict :", ms.groupdict())
        else:
            print("Search: no match")
            
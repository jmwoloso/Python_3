#!/usr/bin/python
#
# Program To Validate Command-Line Zip Code Data
#    zipcheck.py
#
# Created by: Jason Wolosonovich
#    6/01/2015
#
# Lesson 1 - Exercise 3
"""
zipcheck.py: validation function for US zip codes

@author: Jason M Wolosonovich
"""

def zip_errors(z=None):
    """
    Validate zip as either NNNNN or NNNNN-NNNN.
    """
    # check for length of 5 or 10
    if len(z) not in (5, 10):
        return "Zip codes should be 5 or 10 characters long"
    # check that the first 5 characters are digits or if the len is
    # equal to 10, check that the last 4 characters are digits
    if not z[:5].isdigit() or len(z) == 10 and not z[6:].isdigit():
        return "Zip code contains non-numeric characters"
    # if len is 10, check that a hyphen was used to separate first 5
    # characters from last 4 characters
    if len(z) == 10 and z[5] != "-":
        return "Ten-digit zips must have a dash between the two parts"
    return
    
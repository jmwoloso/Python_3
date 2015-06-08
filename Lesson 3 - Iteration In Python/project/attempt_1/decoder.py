#!/usr/bin/python
#
# Program That Uses A Generator To Create Letters
#    decoder.py
#
# Created by: Jason Wolosonovich
#    6/02/2015
#
# Lesson 3 - Project Attempt 1
"""
decoder.py: Uses a generator to encode integers between 1 & 26 into
            capital letters of the alphabet.

@author: Jason M. Wolosonovich
"""
from string import ascii_uppercase
import sys


def alphabator(integer_list):
    if not isinstance(integer_list, (range, list)):
        raise TypeError("'integer_list' must be one of type <list> or <range>")
    for i,integer in enumerate(integer_list):
        if isinstance(integer, int) and 0 < integer < 27:
            yield ascii_uppercase[integer - 1]
        else:
            yield integer

if __name__=="__main__":
    print("Demonstrating Functionality\n")
    # try encoding "correct" values
    a = alphabator(range(1,27))
    print("Encoding numbers as letters where A=1, B=2,...Z=26")
    print(list(a))
    print()
    # try values inside and outside of range
    b = alphabator(range(0,30))
    print("This can handle values outside of specified range as well.")
    print(list(b))
    print()
    # try floats
    c = alphabator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    print("Can also handle floats.")
    print(list(c))
    print()
    # try non-numeric items
    d= alphabator(['lawnmower', 'shovel'])
    print("Non-numeric items are fine too.")
    print(list(d))
    print()
    print("End Demo")
    # end demo
    sys.exit()
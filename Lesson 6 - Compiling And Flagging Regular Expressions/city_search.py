#!/usr/bin/python
#
# Program To Find The City, State And Zip From A Text Using re.compile
#    city_search.py
#
# Created by: Jason M Wolosonovich
#    6/04/2015
#
# Lesson 6 - Exercise 1
"""
city_search.py: Finds the city, state and zip from a text.

@author: Jason M. Wolosonovich
"""
import re

def city_search(text):
    regex = re.compile(r"""
        [A-Z][a-z]+        # the first word of a city
        (\s[A-Z[a-z]+)*   # possible additional words of a city
        ,\s[A-Z]{2}\s     # the two-letter abbreviation for a US state
        \d{5}             # five-digit US zip code
        """, re.VERBOSE)
    search = regex.search(text)
    if search:
        return search.group()
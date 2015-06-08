#!/usr/bin/python
#
# Program To Find The City, State And Zip From A Text
#    city_search.py
#
# Created by: Jason M Wolosonovich
#    6/03/2015
#
# Lesson 5 - Exercise 6
"""
city_search.py: Finds the city, state and zip from a text.

@author: Jason M. Wolosonovich
"""
import re

def city_search(text):
    regex = r"[A-Z][a-z]+(\s[A-Z][a-z]+)*,\s[A-Z]{2}\s\d{5}"
    search = re.search(regex,
                       text)
    if search:
        return search.group()
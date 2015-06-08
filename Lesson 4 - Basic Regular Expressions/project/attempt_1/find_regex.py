#!/usr/bin/python
#
# Program To Find The Start And End Positions Of A Phrase
#    find_regex.py
#
# Created by: Jason Wolosonovich
#    6/03/2015
#
# Lesson 4 - Project Attempt 1
"""
find_regex.py: A program that finds the starting and ending positions
               of a given phrase.
               
@author: Jason M. Wolosonovich
"""
import re

# demo text for main() loop
demo_text=\
"""In the 1950s, mathematician Stephen Cole Kleene described automata
theory and formal language theory in a set of models using a
notation called "regular sets" as a method to do pattern matching.
Active usage of this system, called Regular Expressions, started in
the 1960s and continued under such pioneers as David J. Farber,
Ralph E. Griswold, Ivan P. Polonsky, Ken Thompson, and Henry
Spencer."""

def find_regex(phrase=None, text=demo_text):
    """
    Finds the starting and ending positions of a word or phrase within
    a specified body of text
    """
    #phrase = str(phrase)
    match = re.search(phrase, text)
    if match:
        return tuple((match.start(), match.end()))
    
       
if __name__=="__main__":
    
    phrase = "Regular Expressions"
    match = find_regex(phrase, demo_text)
    print(match)
#!/usr/bin/python
#
# Program To Split Up A Text Into Sentences
#    sentence_split.py
#
# Created by: Jason M Wolosonovich
#    6/03/2015
#
# Lesson 5 - Exercise 10
"""
sentence_split.py: Splits a text up into sentences.

@author: Jason M. Wolosonovich
"""
import re 

def sentence_split(text):
    return re.split(r"[?.!]\s+", text)
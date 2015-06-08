#!/usr/bin/python
#
# A Program To Print Out The Command Line Arguments Of A Script
#    cmdline.py
#
# Created by: Jason Wolosonovich
#    6/01/2015
#
# Lesson 1 - Exercise 1
"""
Simple program to dump the command line arguments
"""
import sys

for n, arg in enumerate(sys.argv):
    print(n, ":", arg)
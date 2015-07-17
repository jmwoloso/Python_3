#!/usr/bin/python
#
# Program To Provide Parse Logging From sys.argv
#    commands.py
#
# Created by: Jason M Wolosonovich
#    6/10/2015
#
# Lesson 12 - Exercise 1
"""
commands.py: Parse logging level options from sys.argv

@author: Jason M. Wolosonovich
"""
from optparse import OptionParser

if __name__=="__main__":
    
    # instantiate OptionParser object
    parser = OptionParser()
    parser.add_option("-l", "--loglevel",
                      action="store",
                      dest="level",
                      default="warning",
                      help="set level of logger: debug, info, "+\
                           "warning (default), error, critical")
    (options, args) = parser.parse_args()
    print("level: {0}".format(options.level))
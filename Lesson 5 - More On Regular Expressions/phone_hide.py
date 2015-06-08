#!/usr/bin/python
#
# A Program To Obscure The Non-Area Code Digits Of A Phone Number
#    phone_hide.py
#
# Created by: Jason M Wolosonovich
#    6/03/2015
#
# Lesson 5 - Exercise 8
"""
phone_hide.py: Hides the digits after the area code in a phone number

@author: Jason M. Wolosonovich
"""
import re 

def phone_hide(text):
    return re.subn(r"\d{3}-\d{4}", "XXX-XXXX", text)
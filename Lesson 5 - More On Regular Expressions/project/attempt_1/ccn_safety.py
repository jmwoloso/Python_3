#!/usr/bin/python
#
# Program To Hide Credit Card Numbers In A Text
#    ccn_safety.py
#
# Created by: Jason M Wolosonovich
#    6/03/2015
#
# Lesson 5 - Project Attempt 1
"""
ccn_safety.py: Obscures credit card information in a text.

@author: Jason M. Wolosonovich
"""
import re 

demo_text = """Have you ever noticed, in television and movies, that phone
numbers and credit cards are obviously fake numbers like 555-123-4567 or
5555-5555-5555-5555-5555? It is because a number that appears to be real, such
as 1234-5678-1234-5678, triggers the attention of privacy and security
experts."""

def ccn_safety(text):
    """
    Obscures one or more credit card numbers in a body of text
    """
    return re.subn(r"\d{4}-\d{4}-\d{4}", "XXXX-XXXX-XXXX", text)
    
if __name__=="__main__":
    print("Text to modify")
    print("\n{0}\n".format(demo_text))
    # obscure cc #s
    safe, count = ccn_safety(demo_text)
    print("\nText after modification")
    print("\n{0}\n".format(safe))
    print("Replacements made: {0}".format(count))
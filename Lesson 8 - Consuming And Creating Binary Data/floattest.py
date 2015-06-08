#!/usr/bin/python
#
# Program To Demonstrate Use Of Floating-Point Values In Files
#    floattest.py
#
# Created by: Jason M Wolosonovich
#    6/04/2015
#
# Lesson 8 - Exercise 1
"""
floattest.py: Demonstrates the use of floating-point values in files.

@author: Jason M. Wolosonovich
"""
import random, os, struct

filename = r"v:\workspace\Python3_Lesson08\src\floatdata.bin"
rlist = [random.random() for i in range(10)]

with open(filename, "wb") as f:
    f.write(struct.pack("=10d", *rlist))
    f.close()

with open(filename, "rb") as f:
    for i in range(10):
        s = f.read(8)
        x, = struct.unpack("=d", s)
        if x != rlist[1]:
            print(i, x, rlist[1], abs(x-rlist[1]))
        else:
            print(i, x, "values agree")
print(filename, os.stat(filename).st_size)

    
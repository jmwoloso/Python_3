#!/usr/bin/python
#
# Program To Print The Timestamp For Each Packet In A Data File
#    wiretimes.py
#
# Created by: Jason M Wolosonovich
#    6/05/2015
#
# Lesson 8 - Project Attempt 1
"""
wiretimes.py: Prints the timestamps for each packet in a data file

@author: Jason M. Wolosonovich
"""
import struct, os


def bin_gen(file, buffer, pos, end):
        """
        Generator function for cycling through a binary file
        """
        while pos < end:
            # read current packet
            v = file.read(buffer)
            # get seconds and milliseconds
            w,x,y,z = struct.unpack("4L", v)
            # skip to next packet
            v = file.read(min(y,z))
            pos = file.tell() 
            yield [w,x]
 

if __name__=="__main__":
    
    filename = r"v:\workspace\Python3_Homework08\src\wireshark.bin"

    with open(filename, "rb") as f:
        # get the file header info out of the way
        f.read(24)
        # view bin file header for info on what buffer size to use
        # for your particular file
        buffer = 16
        # get current file position
        pos = f.tell()
        # get end of file position
        end = os.path.getsize(filename)
        # use generator to cycle through file
        u = bin_gen(f, buffer, pos, end)
        
        for sec, ms in u:
            # 31556926 seconds in a year
            print("timestamp (seconds): {0}".format(sec))
            print("timestamp (milliseconds): {0}\n".format(ms))
        print("End of file")
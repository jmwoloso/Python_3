#!/usr/bin/python
#
# Program To Demonstrate Inheritance
#    furnishings.py
#
# Created by: Jason M Wolosonovich
#    6/04/2015
#
# Lesson 7 - Project Attempt 1
"""
furnishings.py: Demonstrates inheritance

@author: Jason M. Wolosonovich
"""
import sys


class Furnishing(object):
    def __init__(self, room):
        self.room = room
        

class Sofa(Furnishing):
    pass


class Bookshelf(Furnishing):
    pass


class Bed(Furnishing):
    pass


class Table(Furnishing):
    pass


def counter(home):
    """
    Function to count the number of each of the items; returns a tuple
    of form (item, count)
    """
    if not isinstance(home, list):
        raise TypeError("argument 'home' should be of type <list>")
    # dict for plurals
    plural_lookup = {'Furnishing': 'Furnishings',
                     'Sofa': 'Sofas',
                     'Bookshelf': 'Bookshelves',
                     'Bed': 'Beds',
                     'Table': 'Tables'}
    # list of items
    item_list = [item.__class__.__name__ for item in home]
    # set of unique items
    item_set = set(item_list)
    item_tuples = []
    # print them out
    for item in item_set:
        item_tuples.append((item,
                            item_list.count(item)))
        print("{0}: {1}".format(plural_lookup[item],
                                 item_list.count(item)))
    
    return item_tuples


def map_the_home(home):
    """
    Function to map the items in each room; returns a dict where each
    room is a key and the values are the items in each room
    """
    if not isinstance(home, list):
        raise TypeError("argument 'home' should be of type <list>")
    # dict to store home map
    home_map = {}
    # populate home map
    for item in home:
        # set default values to empty lists, if key is found (item.room)
        # then append value (item) to the list, otherwise create
        # key, value pair
        home_map.setdefault(item.room, []).append(item)
    # print the home map
    print(home_map)
    return home_map

if __name__=="__main__":
    home = []
    home.append(Bed('Bedroom'))
    home.append(Sofa('Living Room'))
    home.append(Table('Living Room'))
    home.append(Table('Kitchen'))
    home.append(Bookshelf('Living Room'))
    
    # map the home
    home_map = map_the_home(home)
    
    # get item counts
    item_counts = counter(home)
    #goodbye
    sys.exit()
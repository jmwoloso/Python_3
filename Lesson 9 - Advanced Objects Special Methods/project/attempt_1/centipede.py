#!/usr/bin/python
#
# Program To Demonstrate Special Methods
#    centipede.py
#
# Created by: Jason M Wolosonovich
#    6/05/2015
#
# Lesson 9 - Project Attempt 1
"""
centipede.py: Demonstrates the use of special methods

@author: Jason M. Wolosonovich
"""


class CentipedeMixin(object):       
    """
    Mixin class for centipede.py
    """

    def __init__(self):
        self.legs = []
        self.stomach = []
        
    def __call__(self, *args):
        if args:
            for arg in args:
                arg = str(arg)
                arg = arg.strip("()")
                self.stomach.append(arg)
        
        
class Centipede(CentipedeMixin):
    """
    Mixin class for centipede.py. Comes with 'stomach' and 'legs'
    attributes. 
    
    Batteries not included.
    """
    def __init__(self, *args):
        if args:
            super().__init__()
            super().__call__(*args)
        else:
            super().__init__()
            
                
    def __setattr__(self, name, value):
        # using super's __setattr__ prevents infinite recursion
        # unlike setattr(), at least with this code
        
        # allow setting of 'legs' and 'stomach' upon instantiation
        # but not after, at least via the user
        if name in ['stomach',
                    'legs'
                    ]:
            if not hasattr(self, name):
                super().__setattr__(name, value)
            else:
                raise AttributeError("{0} is for internal use only"\
                                     .format(name))
        else:
            if not hasattr(self, name):
                # create the attribute and append name
                # to 'legs'
                legs_value = self.__dict__['legs']
                legs_value = list(legs_value)
                legs_value.append(name)
                self.__dict__['legs'] = legs_value
                super().__setattr__(name, value)
            elif hasattr(self, name):
                # attribute already exists, so just
                # update value
                super().__setattr__(name, value)
                                
    def __call__(self, *args):
        if args:
            for arg in args:
                self.stomach.append(arg)
    
    def __str__(self):
        # use str generator expression in case the Centipede
        # eats something unusual...like a number...or
        # another Centipede...
        return ",".join(str(item) for item in self.stomach)
    
    def __repr__(self):
        return ",".join(str(item) for item in self.legs)
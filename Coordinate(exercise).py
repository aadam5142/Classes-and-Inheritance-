# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 00:21:44 2020

@author: anwar
"""

#Add an __eq__ method that returns True if coordinates 
#refer to same point in the plane (i.e., have the same x and y coordinate).

#Define __repr__, a special method that returns a string that looks like a 
#valid Python expression that could be used to recreate an object with the same value. 
#In other words, eval(repr(c)) == c given the definition of __eq__ from part 1.

class Coordinate(object):
    def _init_(self,x,y):
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def _eq_(self, other):
        assert type(other) == type(self)
        return self.getX() == other.getX() and self.getY() == other.getY()
    
    def _repr_(self):
        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'
    
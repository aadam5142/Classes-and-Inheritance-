# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 23:17:38 2020

@author: anwar
"""

# Print Representation of an Object

# uniformative print representation by default

# _str_ method for a class
# python calls the _str_ method when used with print on your class object

# Defining your own print method

class Coordinate(object):
    def_init_(self, x, y):
        self.x = x
        self.y = y
    def distance(self, others):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)** 0.5
    def _str_(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    
    
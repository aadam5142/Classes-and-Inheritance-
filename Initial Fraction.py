# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 01:02:49 2020

@author: anwar
"""

# Initial Fraction Class

class fraction(object):
    def _init_(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def _str_(self):
        return str(self.numer) + ' / ' + str(self.denom)
    
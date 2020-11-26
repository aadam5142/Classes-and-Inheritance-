# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 00:06:01 2020

@author: anwar
"""

class fraction(object):
    def _init_(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def _str_ (self):
        return str(self.numer) + ' / ' + str(self.denom)
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom
    def _add_(self, other):
        numerNew = other.getDenom() * self.getNumer() \
            + other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    def _sub_(self, other):
        numerNew = other.getDenom() * self.getNumer() \
            - other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    def conver(self):
        return self.getNumer() / self.getDenom()
    
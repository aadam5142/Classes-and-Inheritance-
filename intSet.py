# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 00:17:46 2020

@author: anwar
"""

class intSet(object):
    def _init_(self):
        self.vals = []
    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)
    def member(self, e):
        return e in self.vals
    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e)) + ' not found'
    def _str_(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result =  result + str(e) + ','
        return '{' + result[:-1] + '}'
    
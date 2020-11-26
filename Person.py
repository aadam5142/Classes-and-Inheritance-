# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 00:40:50 2020

@author: anwar
"""

# Buidling a Class

import datetime 

class Person(object):
    def _init_(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastname = name.split(' ')[-1]
        
    
    def getLastName(self):
        """return self's last name"""
        return self.lastname
    
    def _str_(self):
        """return self's name"""
        return self.name
    
    def setBirthday(self, month, day, year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)
        
    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def _lt_(self, other):
        """return True if self's name is lexicographically
           less than other's name, and Fale otherwise"""
           if self.lastName == other.lastName:
               return self.name < other.name 
           return self.lastName < other.lastName 
    
    def _str_(self):
        """return self's name"""
        return self.name
    
    # example usage
    
    p1 = Person('Mark Zuckerberg')
    p1.setBirthday(5, 14, 84)
    p2 = Person('Drew Houston')
    p2 = setBirthday(3, 4, 83)
    p3 = Person('Bill Gates')
    p3.setBirthday(10, 28, 55) 
    p4 = Person('Andrew Gates')
    p5 = Person('Steve Wozniak')
    
    personList = [p1, p2, p3, p4, p5]
    
    for e in personList:
        print(e)
        
    
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 01:18:12 2020

@author: anwar
"""

# Building Inheritance

class MITPerson(person):
    nextIdNum = 0 # next ID number to assign
    
    def _init_(self, name):
        Person._init_(self, name) #initialize Person attributes
        self.idNum = MITPerson.nextIdNum # MITPerson attributeL unique ID
        MITPerson.nextIdNum += 1
        
    def getIdNum(self):
        return self.idNum
    
    # sorting MIT people uses their ID number, not name!
    def _lt_(self, other):
        return self.idNum < other.idNum
    
    def speak(self, utterance):
        return (self.getLastName() + "says: " + utterance)
    
    def getClass(self):
        return self.year
    
    def speak(self, utterance):
        return MITPerson.speak(self, " Dude, " + utterance)
    
class Student(MITPerson):
    pass

class UG(Student):
    def _init_(self, name, classYear):
        MITPerson._init_(self, name)
        self.year = classYear
        
    def getClass(self):
        return self.year
    def speak(self, utterance):
        return MITPerson.speak(self, " Dude, " + utterance)

    
class Grad(MITPerson):
    pass

    def isStudent(obj):
        return isinstance(obj, UG) or isinstance(obj, Grad)

class TransferStudent(MITPerson):
    pass
def isStudent(obj):
    return isinstance(obj, UG) or isinstance(obj,Grad)

class Professor(MITPerson):
    def _init_(self, name, department):
        MITPerson._init_(self, name)
        self.department = department
        
    def speak(self, utterance):
        new = 'In course ' + self.department + ' we say'
        return MITPerson.speak(self, new + utterance)
    
    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic)
    

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 00:59:18 2020

@author: anwar
"""

import random

class Student(Person):
    def _init_(self, name, age, major-None):
        Person._init_(self, name, age)
        self.major = major
    def change_major(self, major):
        self = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i am watching tv")
    def _str_(self):
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)
    
            
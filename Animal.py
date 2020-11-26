# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 23:01:39 2020

@author: anwar
"""

# Deifining a Class 

#class Animal(object):
#    def _init_(self, age):
#        self.age = age
#        self.name = None
 


# Getter and Setter Methods

class Animal(object):
    def _init_(self, age):
        self.age = age
        self.name = None
    
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name 
    
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname = ""):
        self.name - newname
        
    def _str_(self):
        return "animal:" + str(self.name)+":" + str(self.age)
    
    # Getters and setters should be used outside of class 
    # to access data attributes
    
   # Instantiation create an instance of an object
   # a = Animal(3)
   
   # dot notation usecd to access attribtute (data and metod)
   # though it is better to use getters and setters to acces data attributes
   
   # a.age
   # a.get_age()
   
   # if you are accessing data attributes outside the class and class
   # definition changes, may get errors
   
   # Outside of class, use getters and setters instead 
       # use a.get_age() Not a.age
     
class Cat(Animal):
    def speak(self):
        print("meow")
    def _str_(self):
        return "cat:" + str(self.name)+":"+str(self)

class Rabbit(Animal):
    def speak(self):
        print("meep")
    def _str_(self):
        return "rabbit:" + str(self.name) + ":" + str(self.age)
    
class Person(Animal):
    def _init_ (self, name, age):
        Animal._init_(self, age)
        Animal.set_name(self, name)
        self.friends = []
        
    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self, other):
        # alternate way: diff = self.age - other.age
        diff = self.get_age() - other.get()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
                print(self.name, "is", -diff, "years younger than", other.name)
    def _str_(self):
        return "person:" + str(self.name) + ":" + str(self.age)
    
    
import random

class Student(Person):
    def _init_(self, name, age, major = None):
        Person._init_(self, name, age)
        self.major = major
    def change_major = (self, major):
        self = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r <0.75:
            print("i should eat")
        else:
            print("i am watching tv")
    def _str_9(self):
        return "student:" + str(self.name)+":" + str(self.age)+":"+str(self.major)

# Rabbit Getter Methods

class Rabbit(Animal):
    tag = 1
    def _init_(self,age, parent1 = None, parent2 = None):
        Animal._init_(self, age)
        self.parent1 = parent1
        self.parent2 = parent2 
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    def get_rid(self):
        return str(self.rid).zfill(3)
    def get_get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    
    def _add_(self, other):
        # returning object of same type as this class
        return Rabbit(0, self, other)
    
    # Special method to Compare Two Rabbits
    
    # Decide that two rabbits are equal if they have the same two parents
    
    def _eq_(self, other):
        parents_same = self.parent1.rid == other.parent1.rid \ 
                       and self.parent2.rid == other.parent.rid 
                       
        parents_opposite = self.parent2.rid == other.parent1.rid \
                           and self.parent1.rid == other.parent2.rid 
                          
        return parents_same or parents_opposite 
    
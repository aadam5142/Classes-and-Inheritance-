# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 18:29:47 2020

@author: anwar
"""

#__init__(self, text, shift): Use the parent class constructor to make your code more concise.
#The getter method get_shift(self)
#The getter method get_encrypting_dict(self): This should return a COPY of self.encrypting_dict to prevent someone from mutating the original dictionary.
#The getter method get_message_text_encrypted(self)
#change_shift(self, shift): Think about what other methods you can use to make this easier. It shouldn’t take more than a couple lines of code.
#Paste your implementation of the entire PlaintextMessage class in the box below.

class Plaintextmessage(Message):
    def _init_(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message
        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)
        '''
        
        self.shift = shift
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.encrypting_dict = super(PlaintextMessage, self).build_shift_dict(shift)
        self.message_text_encrypted = super(PlaintextMessage, self).apply_shift(shift)
        
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        
        '''
        return self.shift
    
    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        
        encrypting_dict_copy = self.encrypting_dict.copy()
        return encrypting_dict_copy
    
    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        
    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26
        Returns: nothing
        '''
        
        self.shift = shift
        self.encrypting_dict = super(PlaintextMessage, self).build_shift_dict(shift)
        self.message_text_encrypted = super(PlaintextMessage, self).apply_shift(shift)
        
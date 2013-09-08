'''
Created on Sep 8, 2013

@author: maria
'''

class RomanNumber(object):
    digits = {1 : "I", 5 : "V", 10 : "X"}


    def __init__(self, number):
        self.number = number

    
    def text(self):
        return self.digits[self.number]
    
    


'''
Created on Sep 8, 2013

@author: maria
'''

from collections import defaultdict

class RomanNumber(object):
    digits = defaultdict(lambda: "", {1 : "I", 5 : "V", 10 : "X", 50: "L", 100: "C", 500: "D", 1000: "M"})


    def __init__(self, number):
        self.number = number

    
    def text(self):
        result = self.digits[self.number]
        if result == '':
            result = self.digits[self.number / 2] * 2
        if result == '':
            result = self.digits[self.number / 3] * 3
        return result   
    
    

print repr(RomanNumber.digits[0])
'''
Created on Sep 8, 2013

@author: maria
'''

class RomanNumber(object):
    digits = {1 : "I", 5 : "V", 10 : "X", 50: "L", 100: "C", 500: "D", 1000: "M"}


    def __init__(self, number):
        self.number = number

    
    def text(self):
        result = self.digits.get(self.number)
        if result == None:
            result = self.digits.get(self.number / 2) * 2
        return result   
    
    


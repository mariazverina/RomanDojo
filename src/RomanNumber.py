'''
Created on Sep 8, 2013

@author: maria
'''

from collections import defaultdict

class RomanNumber(object):
    digits = defaultdict(lambda: "", {1 : "I", 5 : "V", 10 : "X", 50: "L", 100: "C", 500: "D", 1000: "M"})


    def __init__(self, number):
        self.number = number

    

    @staticmethod
    def digitValue(number):
        return RomanNumber.digits[number]

    def text(self):
        for i in range(1, 4):
            result = self.digitValue(self.number / i) * i
            if result != '':
                break
        return result   
    
    

print repr(RomanNumber.digits[0])
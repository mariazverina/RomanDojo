'''
Created on Sep 8, 2013

@author: maria
'''

from collections import defaultdict

class RomanNumber(object):
    digits = defaultdict(lambda: "", {1: "I",  5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M",
                                      4: "IV", 9: "IX", 40: "XL", 90: "XC", 400:"CD", 900: "CM"})
    divisors = sorted(digits.keys(), reverse=True)


    def __init__(self, number):
        self.number = number

    @staticmethod
    def romanSymbol(number):
        return RomanNumber.digits[number]

    @staticmethod
    def romanEncode(number):
        result = ''
        for divisor in RomanNumber.divisors:
            digitCount = number / divisor
            number = number - digitCount * divisor
            result += RomanNumber.romanSymbol(divisor) * digitCount
        return result   
            
    def text(self):
        return self.romanEncode(self.number)

    
    

print repr(RomanNumber.digits[0])
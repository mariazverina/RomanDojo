'''
Created on Sep 8, 2013

@author: maria
'''
import unittest
from RomanNumber import RomanNumber


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testRoman1isI(self):
        one = RomanNumber(1)
        self.assertEqual(one.text(), "I")

    def testRoman5isV(self):
        five = RomanNumber(5)
        self.assertEqual(five.text(), "V")

    def testRoman10isX(self):
        ten = RomanNumber(10)
        self.assertEqual(ten.text(), "X")
    
    def testRoman50isL(self):
        fifty = RomanNumber(50)
        self.assertEqual(fifty.text(), "L")
    
    def testRoman100isC(self):
        hundred = RomanNumber(100)
        self.assertEqual(hundred.text(), "C")
    
    def testRoman500isD(self):
        fiveHundred = RomanNumber(500)
        self.assertEqual(fiveHundred.text(), "D")

    def testRoman1000isM(self):
        thousand = RomanNumber(1000)
        self.assertEqual(thousand.text(), "M")
        
    def testDoubleDigitRepetition(self):
        twenty = RomanNumber(20)
        self.assertEqual(twenty.text(), "XX")
        
    def testTripleDigitRepetition(self):
        threeHundred = RomanNumber(300)
        self.assertEqual(threeHundred.text(), "CCC")
         
    def testRoman0isEmptyString(self):
        zero = RomanNumber(0)
        self.assertEqual(zero.text(), "")
        
    def testSimpleCombination(self):
        six = RomanNumber(6)
        self.assertEqual(six.text(), "VI")        
        
    def testLongCombination(self):
        sixsixsix = RomanNumber(666)
        self.assertEqual(sixsixsix.text(), "DCLXVI")        

    def testRoman3001isMMMI(self):
        n3001 = RomanNumber(3001)
        self.assertEqual(n3001.text(), "MMMI")
        
    def testRoman4isIV(self):
        four = RomanNumber(4)
        self.assertEqual(four.text(), "IV")
        
    def testRoman9isIX(self):
        nine = RomanNumber(9)
        self.assertEqual(nine.text(), "IX")
        
    def testRoman1999isMCMXCIX(self):
        n1999 = RomanNumber(1999)
        self.assertEqual(n1999.text(), "MCMXCIX")
        
    def testRoman444isCDXLIV(self):
        self.assertEqual(RomanNumber(444).text(), "CDXLIV")
        
    def testBonusTest(self):
        self.assertEqual(RomanNumber(1900).text(), "MCM"),
        self.assertEqual(RomanNumber(1975).text(), "MCMLXXV"),
        self.assertEqual(RomanNumber(1989).text(), "MCMLXXXIX"),
        self.assertEqual(RomanNumber(1999).text(), "MCMXCIX"),
        self.assertEqual(RomanNumber(2000).text(), "MM"),
        self.assertEqual(RomanNumber(2001).text(), "MMI"),


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
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
        self.assertEqual(RomanNumber(1).text(), "I")

    def testRoman5isV(self):
        self.assertEqual(RomanNumber(5).text(), "V")

    def testRoman10isX(self):
        self.assertEqual(RomanNumber(10).text(), "X")
    
    def testRoman50isL(self):
        self.assertEqual(RomanNumber(50).text(), "L")
    
    def testRoman100isC(self):
        self.assertEqual(RomanNumber(100).text(), "C")
    
    def testRoman500isD(self):
        self.assertEqual(RomanNumber(500).text(), "D")

    def testRoman1000isM(self):
        self.assertEqual(RomanNumber(1000).text(), "M")
        
    def testDoubleDigitRepetition(self):
        self.assertEqual(RomanNumber(20).text(), "XX")
        
    def testTripleDigitRepetition(self):
        self.assertEqual(RomanNumber(300).text(), "CCC")
         
    def testRoman0isEmptyString(self):
        self.assertEqual(RomanNumber(0).text(), "")
        
    def testSimpleCombination(self):
        self.assertEqual(RomanNumber(6).text(), "VI")        
        
    def testLongCombination(self):
        self.assertEqual(RomanNumber(666).text(), "DCLXVI")        

    def testRoman3001isMMMI(self):
        self.assertEqual(RomanNumber(3001).text(), "MMMI")
        
    def testRoman4isIV(self):
        self.assertEqual(RomanNumber(4).text(), "IV")
        
    def testRoman9isIX(self):
        self.assertEqual(RomanNumber(9).text(), "IX")
        
    def testRoman1999isMCMXCIX(self):
        self.assertEqual(RomanNumber(1999).text(), "MCMXCIX")
        
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
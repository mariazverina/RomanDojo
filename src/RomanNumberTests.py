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
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
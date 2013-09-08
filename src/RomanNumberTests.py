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
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
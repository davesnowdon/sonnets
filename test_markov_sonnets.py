'''
Created on 8 Nov 2013

@author: dns
'''
import unittest
from markov_sonnets import nsyl, get_num_syllables


class TestSyllables(unittest.TestCase):

    def testHello(self):
        self.assertEqual(2, nsyl("hello"), "Hello has 2 syllables")

    def testHi(self):
        self.assertEqual(1, nsyl("hi"), "Hi has 1 syllable")

    def testSonnet(self):
        self.assertEqual(2, nsyl("sonnet"), "Sonnet has 2 syllables")

    def testShakespeare(self):
        self.assertEqual(2, nsyl("shakespeare"), "Shakespeare has 2 syllables")

    def testSonnetPhrase(self):
        phrase = ['Shall', 'I', 'compare', 'thee', 'to', 'a', 'summer\'s', 'day?']
        self.assertEqual(10, get_num_syllables(phrase), "'Shall I compare thee to a summer's day?' has 10 syllables")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
import unittest
from algorithms.multiplication import multiply

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(add(5,5), 25)
        self.assertEqual(add(1,5), 5)
        self.assertEqual(add(4,5), 20)
        self.assertEqual(add(7,100), 700)
        self.assertEqual(add(0,5), 0)

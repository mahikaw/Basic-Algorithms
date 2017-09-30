import unittest
from algorithms.subtraction import subtract

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(subtract(5,5), 0)
        self.assertEqual(subtract(1,5), -4)
        self.assertEqual(subtract(43,5), 38)
        self.assertEqual(subtract(76,5), 71)
        self.assertEqual(subtract(0,5), -5)

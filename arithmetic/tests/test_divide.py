import unittest
import arithmetic.divide as divide

class TestDivide (unittest.TestCase):
    def test_division(self):
        self.assertEqual (divide.division(100,5), 20)




import arithmetic.multiply as multiply
import unittest

class TestMultiply (unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual (multiply.multiplication(3,4), 12)


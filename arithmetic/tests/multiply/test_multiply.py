import arithmetic.multiplication.multiply as multiply
import pytest

class TestMultiply:
    def test_multiplication(self):
        assert multiply.compute(3,4) == 12



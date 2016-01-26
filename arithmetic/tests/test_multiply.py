import arithmetic.multiply as multiply
import pytest

class TestMultiply:
    def test_multiplication(self):
        assert multiply.multiplication(3,4) == 12



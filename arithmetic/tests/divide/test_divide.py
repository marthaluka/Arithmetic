import pytest
import arithmetic.division.divide as divide

class TestDivide ():
    def test_division(self):
        assert divide.compute(100,5) == 20


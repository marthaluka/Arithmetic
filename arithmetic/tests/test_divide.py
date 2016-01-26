import pytest
import arithmetic.divide as divide

class TestDivide ():
    def test_division(self):
        assert divide.division(100,5) == 20


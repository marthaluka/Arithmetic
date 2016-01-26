# Run all the tests as one.

import arithmetic.tests.test_multiply as test_multiply
import arithmetic.tests.test_divide as test_divide

def main ():
    mul = test_multiply.TestMultiply()
    mul.test_multiplication()
    div = test_divide.TestDivide()
    div.test_division()

if __name__ == "__main__":
    print ("Running all tests...")
    if main () == None:
        print ("Tests ran successfully")

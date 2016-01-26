import arithmetic.multiply as multiply
import arithmetic.divide as divide

def main (a, b):
    mult = multiply.multiplication (a,b)
    div = divide.division(a,b)
    print ("multiplication of %s and %s is: %s" % (a, b, mult))
    print ("division of %s by %s is: %s " % (a, b, div))
    


if __name__ == "__main__":
    main (20,5)
    

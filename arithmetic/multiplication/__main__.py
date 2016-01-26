import arithmetic.multiply.multiply as multiply


def main (a, b):
    mult = multiply.compute (a,b)
    print ("multiplication of %s and %s is: %s" % (a, b, mult))

if __name__ == "__main__":
    main (20,5)
    

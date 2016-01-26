import arithmetic.divide.divide as divide

def main (a, b):
    div = divide.compute(a,b)
    print ("division of %s by %s is: %s " % (a, b, div))
    


if __name__ == "__main__":
    main (20,5)
    

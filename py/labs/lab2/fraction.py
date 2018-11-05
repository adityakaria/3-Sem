class Fraction:

    def __init__(self,numx,denx):
    	self.num=numx
    	self.den=denx

    def inverse(self):
        """Returns the inverse of this Fraction"""
        numx = self.den
        denx = self.num
        return Fraction(numx,denx)

    def add(self,f):
        """Adds the Fraction f to this Fraction and returns the result"""
        numx = (self.num*f.den) + (self.den*f.num)
        denx = self.den*f.den
        return Fraction(numx,denx)

    def subtract(self,f):
        """Subtracts the Fraction f from this Fraction and returns the result"""
        numx = (self.num*f.den) - (self.den*f.num)
        denx = self.den*f.den
        return Fraction(numx,denx)


    def multiply(self,f):
        """Multiplies the Fraction f to this Fraction and returns the result"""
        numx = (self.num*f.num)
        denx = (self.den*f.den)
        return Fraction(numx,denx)

    def divide(self,f):
        """Divides the Fraction f from this Fraction and returns the result"""
        numx = (self.num*f.den)
        denx = (self.den*f.num)
        return Fraction(numx,denx)

    def __str__(self):
        """Returns a string representation of this fraction"""
        strx = (str(self.num) + "/" + str(self.den))
        return strx

def main():
    f1 = Fraction(2,3)
    print('Fraction 1 is', f1)
    f2 = Fraction(3,4)
    print('Fraction 2 is', f2)
    print('The inverse of f1 is', f1.inverse())
    print('The inverse of f2 is', f2.inverse())
    print('f1+f2 is', f1.add(f2))
    print('f1-f2 is', f1.subtract(f2))
    print('f1 * f2 is', f1.multiply(f2))
    print('f1 / f2 is', f1.divide(f2))

if __name__ == '__main__':
    main()

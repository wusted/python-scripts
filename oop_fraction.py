class Fraction:
    """ Class representation of a Mathematical Fraction. """
    
    def __init__(self, top, bottom):
        self.num = top      # the numerator is on top
        self.den = bottom   # the denominator is on the bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

myfraction = Fraction(3, 4)
print(myfraction)

print(myfraction.getNum() , "is the Numerator")
print(myfraction.getDen() , "is the Denominator")


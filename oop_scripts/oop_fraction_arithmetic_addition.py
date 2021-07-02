def greatest_common_denominator(numerator, denominator):
    while numerator % denominator != 0:
        oldnum = numerator
        oldden = denominator

        numerator = oldden
        denominator = oldnum % oldden

    return denominator

class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def simplify(self):
        common = greatest_common_denominator(self.num, self.den)

        self.num = self.num // common
        self.den = self.den // common

    def add(self,otherfraction): # We could also use __add__ and invoke the method with "+" instead of object.method
        
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den

        common = greatest_common_denominator(newnum, newden)

        return Fraction(newnum // common, newden // common)

f1 = Fraction(1, 2)
f2 = Fraction(1, 4)
print("Fraction 1:", f1, "   Fraction 2:", f2)


f3 = f1.add(f2) # Here is where could use "+" instead of add if __add__ method.
print("Their fraction sum is: ", f3)

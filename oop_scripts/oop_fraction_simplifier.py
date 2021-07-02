def greatest_common_divisor(numerator, denominator):
    while numerator % denominator != 0:
        oldnum = numerator
        oldden = denominator

        numerator = oldden
        denominator = oldnum % oldden

    return denominator

class Fraction:

    def __init__(self, top, bottom):
        self.num = top      # the numerator is on top
        self.den = bottom   # the denominator is on bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def simplify(self):
        common = greatest_common_divisor(self.num, self.den)

        self.num = self.num // common
        self.den = self.den // common

nume = int(input("Please enter the numerator for the fraction: "))
deno = int(input("Please enter the denominator for the fraction: "))
myfraction = Fraction(nume, deno)

print("The fraction is: ", myfraction)
myfraction.simplify()
print("Can be simplified to: ", myfraction)


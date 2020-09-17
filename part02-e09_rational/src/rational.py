#!/usr/bin/env python3

class Rational(object):

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.number = self.numerator/self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_numerator = int(self.numerator)*int(other.denominator) + int(self.denominator)*int(other.numerator)
        new_denominator = int(self.denominator)*int(other.denominator)
        return Rational(new_numerator, new_denominator)
         
    def __sub__(self, other):
        new_numerator = int(self.numerator)*int(other.denominator) - int(self.denominator)*int(other.numerator)
        new_denominator = int(self.denominator)*int(other.denominator)
        return Rational(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = int(self.numerator)*int(other.numerator)
        new_denominator = int(self.denominator)*int(other.denominator)
        return Rational(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = int(self.numerator)*int(other.denominator)
        new_denominator = int(self.denominator)*int(other.numerator)
        return Rational(new_numerator, new_denominator)
    
    def __eq__(self, other):
        return float(self.number) == float(other.number)
    
    def __gt__(self, other):
        return float(self.number) > float(other.number)
    
    def __lt__(self, other):
        return float(self.number) < float(other.number)

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()

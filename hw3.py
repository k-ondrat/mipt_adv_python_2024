import numpy as np

class Complex:
    def __init__(self, real_part, imaginary_part):
        self.imaginary_part =  imaginary_part
        self.real_part = real_part
    def Expon(self):
        r = (self.real_part**2 + self.imaginary_part**2)**0.5
        fi = np.arccos(self.real_part/self.imaginary_part)
        return self.r, self.fi
    
def summ (complex1, complex2):
    a = complex1.real_part + complex2.real_part
    b = complex1.imaginary_part + complex2.imaginary_part
    z = Complex(a,b)
    return z

def diff (complex1, complex2):
    a = complex1.real_part - complex2.real_part
    b = complex1.imaginary_part - complex2.imaginary_part
    z = Complex(a,b)
    return z

def multiple (complex1, complex2):
    a = complex1.real_part * complex2.real_part - complex1.imaginary_part * complex2.imaginary_part
    b = complex1.imaginary_part * complex2.real_part + complex1.real_part * complex2.imaginary_part
    z = Complex(a,b)
    return z

def division (complex1, complex2):
    if complex2.real_part**2 + complex2.imaginary_part**2 != 0:
        a = (complex1.real_part * complex2.real_part + complex1.imaginary_part * complex2.imaginary_part)/(complex2.real_part**2 + complex2.imaginary_part**2)
        b = (complex1.imaginary_part * complex2.real_part - complex1.real_part * complex2.imaginary_part)/(complex2.real_part**2 + complex2.imaginary_part**2)
        z = Complex(a,b)
        return z
    else:
        print("Error: division by zero")
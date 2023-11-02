class Complex:
    
    def __init__(self, r, i):
        self.imaginary = i
        self.real = r
    def __add__(self,c):
        return complex(self.real + c.real, self.imaginary + c.imaginary)
    def __mul__(self, c):
        mulReal = self.real*c.real - self.imaginary * c.imaginary
        mulImag = self.real * c.imaginary - self.imaginary * c.real
        return complex(mulReal, mulImag)
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
    
c1 = Complex(4, 3)
c2 = Complex(3, 5)
print(c1 + c2)      
print(c1 * c2)      



class Calculator:
    def __init__(self, num):
        self.number = num
        
    def sqrt(self):
        print(f"Square Root of {self.number} is {self.number**0.5}")
    def sqr(self):
        print(f"Square of {self.number} is {self.number**2}")
    def cube(self):
        print(f"Cube of {self.number} is {self.number**3}")
        
number = Calculator(25)
number.sqrt()
number.sqr()
number.cube()
        
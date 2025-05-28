import math

class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

    def __mul__(self, other):
        return Calculator(self.value * other.value)

    def __truediv__(self, other):
        return Calculator(self.value / other.value)

    def __pow__(self, other):
        return Calculator(self.value ** other.value)

    def log(self, base):
        return Calculator(math.log(self.value, base.value))

    def __str__(self):
        return str(self.value)

a = Calculator(10)
b = Calculator(2)

print(a + b)        
print(a - b)        
print(a * b)        
print(a / b)        
print(a ** b)       
print(a.log(b))     
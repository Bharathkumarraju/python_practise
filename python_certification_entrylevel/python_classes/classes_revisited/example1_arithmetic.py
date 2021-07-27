class Arithmetic:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        res = self.a + self.b
        return res
    def sub(self):
        res = self.a - self.b
        return res
    def mul(self):
        res = self.a * self.b
        return res
    def div(self):
        res = self.a / self.b
        return res

arith = Arithmetic(10, 20)

addition = arith.add()
print("Addition is ", addition)

subtraction = arith.sub()
print("Subtraction is", subtraction)

multiplication = arith.mul()
print("Multiplication is", multiplication)

division  = arith.div()
print("The division is", division)
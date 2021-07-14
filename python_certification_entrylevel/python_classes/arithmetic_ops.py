class Arithmetic_Ops:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        addition = self.a + self.b
        return addition
    def substract(self):
        sub = self.a - self.b
        return sub
    def multiply(self):
        mul = self.a * self.b
        return  mul
    def divide(self):
        div = self.a / self.b
        return div

arith = Arithmetic_Ops(12, 7)

add_of_two_numbers = arith.add()
print(add_of_two_numbers)

sub_of_two_numbers = arith.substract()
print(sub_of_two_numbers)

mul_of_two_numbers = arith.multiply()
print(mul_of_two_numbers)

div_of_two_numbers = arith.divide()
print(div_of_two_numbers)
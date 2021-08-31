class A:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def add(self):
        result = self.a + self.b
        return result

number1 = int(input("Enter a first number!"))
number2 = int(input("Enter a second number!"))

x = A(number1, number2)
res = x.add()

print("the addition of", number1, "and", number2, "is: ", res)
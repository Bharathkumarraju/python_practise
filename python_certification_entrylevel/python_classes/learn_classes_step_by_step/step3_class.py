class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, number):
        real = self.real + number.real
        imag = self.imag + number.imag
        result = Complex(real, imag)
        return result


n1 = Complex(5, 6)
n2 = Complex(-4, 2)

res = n1.add(n2)
print("real = ", res.real)
print("imag = ", res.imag)
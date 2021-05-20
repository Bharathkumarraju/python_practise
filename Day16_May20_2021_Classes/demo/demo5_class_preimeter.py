class triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        perimeter = self.a + self.b + self.c
        return perimeter

t1 = triangle(10, 11, 10)

perimeter = t1.get_perimeter()
print("The perimeter is: ", perimeter)



class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def permiter(self):
        self.perimeter = self.a + self.b + self.c
    def print_sum(self):
        print(self.perimeter)

t1 = Triangle(10, 20, 90)
t1.permiter()
t1.print_sum()

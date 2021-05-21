class triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # def set_perimeter(self):
    #     self.perimeter = self.a  + self.b + self.c

    def get_perimeter(self):
        perimeter = self.a + self.b + self.c
        return perimeter

t1 = triangle(10, 10, 10)
result = t1.get_perimeter()
print("The permiter of three sides of tringle is {} ".format(result))

class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sum(self):
        self.sum = self.a + self.b

    def display_sum(self):
        print(self.sum)


a = A(1000, 2000)
a.get_sum()
a.display_sum()
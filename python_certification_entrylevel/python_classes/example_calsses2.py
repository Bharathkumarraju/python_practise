class bk_add:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        res=self.a + self.b
        return res

# one way
addition = bk_add(10,8).add()
print(addition)

# another way
add1 = bk_add(1000, 2000)
ressult = add1.add()
print(ressult)

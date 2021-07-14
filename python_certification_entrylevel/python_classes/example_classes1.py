class Test:
    def __init__(self, i, j):
        self.a = i
        self.b = j
        a = 11
        print(a)
        self.main()
        print(self.a)
        print(self.b)

    def main(self):
        pass

test_variable = Test(100, 110)
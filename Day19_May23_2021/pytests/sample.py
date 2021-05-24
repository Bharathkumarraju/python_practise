class One:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        if isinstance(self.a, int) and isinstance(self.b , str):
            self.a = str(self.a)
        elif isinstance(self.a, str) and isinstance(self.b, int):
            self.b = str(self.b)
        self.sum = self.a + self.b
        return self.sum

    def multilply(self):
        if isinstance(self.a, str) and isinstance(self.b, str):
            raise TypeError
        if isinstance(self.a, int) and isinstance(self.b, str):
            if self.a < 0 :
                raise ValueError
        elif isinstance(self.b, int) and isinstance(self.a, str):
            if self.b < 0:
                raise ValueError

        if isinstance(self.a, float) and isinstance(self.b, str):
            if self.a < 0 :
                raise TypeError
        elif isinstance(self.b, float) and isinstance(self.a, str):
            if self.b < 0:
                raise TypeError

        self.mul = self.a * self.b
        return self.mul



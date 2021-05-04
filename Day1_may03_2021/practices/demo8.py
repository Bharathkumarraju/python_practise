class test:
    def __init__(self,j):
        self.a = j  # the scope is whole class.
        self.b = 12 # the scope is whole class.
        a = 890 # The scope is local.
        self.main() # The scope is whole class.
        print(self.a) # The scope is whole class.
        print(a) # The scope is local.

    def main(self):
        print(self.a) # The scope is whole class.

test_variable = test(1323)

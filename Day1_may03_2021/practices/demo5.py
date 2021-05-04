# class is called user defined data type.
class test:
    def __init__(self,i):
        a = 5 # scope will be in the only inside __init__ function
        b = 6
        self.a = 35345
        print(self.a)
        self.a = i
#        self.a = 100 # this scope is for the whole class
#       self.main()
#        print(self.a)
#        print(a)
    def main(self):
        print(self.a)
#        print(a)


#print(test.a)
custom_variable = test(3463)
custom_variable.main()
#print(custom_variable)

#print(self.a)
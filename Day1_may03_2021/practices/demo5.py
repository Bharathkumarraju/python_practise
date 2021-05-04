# class is called user defined data type.
class test:
    def __init__(self,i):
        a = 5 # scope will be in the only inside __init__ function
        b = 6
        self.a = 33
        print(self.a) # Just for debugging
        self.a = i # this scope will be whole class
        self.main() # main function scope should be whole class that why we have to use self.mai()
#        self.a = 100 # this scope is for the whole class
#       self.main()
#        print(self.a)
#        print(a)
    def main(self):
        print(self.a)
#        print(a)


#print(test.a)
custom_variable = test(18)
#custom_variable.main()
#print(custom_variable)

#print(self.a)
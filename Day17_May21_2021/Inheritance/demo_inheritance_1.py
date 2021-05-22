class animal:
    def eat(self):
        print("I can eat")

class dog(animal):
    def bark(self):
        print("I can bark")

class cat(animal):
    def get_grumpy(self):
        print("I am getting grumpy")

dog1 = dog()
dog1.bark()
dog1.eat()

cat1 = cat()
cat1.eat()
cat1.bark()
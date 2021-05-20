class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name

    def display_name(self):
        print(self.name)

class employee(person):
    def display_emplyer_name(self):
        print(self.employer)

    def set_employer_name(self, employer_name):  # Setters
        self.employer_name = employer_name

    def get_employer_name(self):    # Getters
        return self.employer_name

# e1 = employee("microsoft", 12345)
# e1.display_emplyer_name()
# e1.set_employer_name("bharath")
# print(e1.employer_name)

p1 = person("sakar", 22)
p1.display_name()

p1.set_name("hello")
p1.display_name()

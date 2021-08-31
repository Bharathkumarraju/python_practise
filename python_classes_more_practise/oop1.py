# why need oops

# position, name, age, level, salary

se1 = ["software engineer", "Bharath", 35, "Junior", 5000]
se2 = ["software engineer", "Gnanam", 45, "Senior", 15000]
d1 = ["Designer", "Junkang"]

'''
def code(se):
    print(f"{se[1]} is writing code")

code(se1)
code(se2)
code(d1)
'''

print("")


# class
class SoftwareEngineer:
    # class attribute
    alias = "Keyboard Magician"

    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance method
    def code(self):
        print(f"{self.name} is writing code ...")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}")

    #  def information(self):
    #     information = f"name = {self.name}, age = {self.age}, level={self.level}"
    #     return information

    def __str__(self):
        information = f"name={self.name}, age={self.age}, level={self.level}"
        return information

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000


# instance of the class
se1 = SoftwareEngineer("Bharath", 35, "Junior", 5000)
print(se1.name, se1.age)
print(se1.alias)
print(SoftwareEngineer.alias)
print("")
# print(SoftwareEngineer.age)
se2 = SoftwareEngineer("Gnanam", 45, "Senior", 15000)
se3 = SoftwareEngineer("Gnanam", 44, "Senior", 15000)
print(se2.alias, se2.name, se2.age, se2.level, se2.salary)
print(SoftwareEngineer.alias)
print("")
# Calling instance method from an object

se1.code()
se2.code()

print("")

se1.code_in_language("Java")
se2.code_in_language("Python")

# print(se1.information())

print(se1)
print(se2)

print(se2 == se3)  # its comparing the memory address

print(se1.entry_salary(35))
print(SoftwareEngineer.entry_salary(27))



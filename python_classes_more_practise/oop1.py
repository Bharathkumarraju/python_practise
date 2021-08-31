# why need oops

# position, name, age, level, salary

se1 = ["software engineer", "Bharath", 35, "Junior", 5000]
se2 = ["software engineer", "Lisa", 45, "Senior", 15000]


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


# instance of the class
se1 = SoftwareEngineer("Bharath", 35, "Junior", 5000)
print(se1.name, se1.age)
print(se1.alias)
print(SoftwareEngineer.alias)
# print(SoftwareEngineer.age)



# init method is a special method that automatically gets called everytime objects are created.


class Student:
    def __init__(self, name, marks): # Automatically Initializes the attributes name and marks
        self.name = name
        self.marks = marks
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False

student1 = Student("Harry", 85)
print("The name is: ", student1.name)
print("the marks are: ", student1.marks)
print("and is he pass? ",student1.check_pass_fail())

print("-------------------------")

student2 = Student("Janet", 30)
print(student2.name)
print(student2.marks)
print(student2.check_pass_fail())

print("-------------------------")

student3 = Student("Bharath", 10)
did_pass=student3.check_pass_fail()
print(did_pass)
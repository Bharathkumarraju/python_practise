# When working with objects variables are called attributes and functions are called methods.

# Variables ---> Attributes
# functions ---> methods

class Student:
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False


student1 = Student() # Object Creation
student1.name = "Harry"
student1.marks = 85

did_pass = student1.check_pass_fail()
print(did_pass)

student2 = Student()
student2.name = "janet"
student2.marks = 35

did_pass = student2.check_pass_fail()
print(did_pass)

#print(student1.name)
#print(student1.marks)

#student2 = Student()


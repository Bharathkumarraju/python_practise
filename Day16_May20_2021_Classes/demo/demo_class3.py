
"""
adding attributes to the object manually after defining it is not a good practise at all.
to solve this we use __init__ method.
__init__ method is a special method that automatically gets called when objects are created.
"""

# this "self" represents the object calling it, In our case "self" refers to the student1 object.
class student:
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False
# Remember the first parmater self represents the object calling it, the second(name) and third argument(marks) take the two arguments which we used during the object creation.
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

student1 = student("Bharath", 85)
student2 = student("Hanuman", 39)
print("student name is: ", student1.name)
print("is", student1.name ,"passed? ")
did_pass = student1.check_pass_fail()
print(did_pass)

print("Student name is: ", student2.name)
print("is", student2.name, "passed? ")
did_pass = student2.check_pass_fail()
print(did_pass)


# did_pass = student1.check_pass_fail()
# print(did_pass)

'''
student1 = student()
student1.name = "Bhajrang"
student1.marks = 89
did_pass = student1.check_pass_fail()
print(did_pass)

student2 = student()
student2.name = "Anjaneyam"
student2.marks = 34
did_pass = student2.check_pass_fail()
print(did_pass)
'''

"""
adding attributes to the object manually after defining it is not a good practise at all.
to solve this we use __init__ method.
__init__ method is a special method that automatically gets called when objects are created.
"""
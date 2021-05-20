class student:
    def check_pass_fail(self):
        if self.marks >=40:
            return True
        else:
            return False

student1 = student()
student1.name="bharath"
student1.marks=90
did_pass = student1.check_pass_fail()
print(did_pass)

"""
Method definition has an argument called self(in line2), 
Well, whenever we define methods(check_pass_fail) for a class, we need to use "self" as first argument

this "self" represents the object calling it, In our case "self" refers to the student1 object. and "self.marks" refers to the 'marks' attribute of the 'student1' object i.e. "student1.marks=20"
 
"""

student2 = student()
student2.name="hanuman"
student2.marks=35
did_pass=student2.check_pass_fail()
print(did_pass)

"""
Adding attributes to the object manually after defining it, is not a good practise.
Instead python offers much more elegant and compact way of defining attributes, right while instantiating the object.

For that python provides a method called "__init__()"
init method is a special method that automatically gets called everytime objects are created.
"""
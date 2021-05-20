class student:
    pass

student1 = student()

student1.name = "harry"
student1.marks = 85

print(student1.name)
print(student1.marks)

"""

However this is not the proper way to add attributes to objects.
Usually what we wanted do is
we want to put all the attributes(name, marks) inside of the class, so that all the objects created from the class have these attributes(name,marks) by default.

Similarly we also put all the methods inside a class, so that every object of the class can access them.

1. How to add methods inside a class.
2. Then how to add attributes inside a class


"""
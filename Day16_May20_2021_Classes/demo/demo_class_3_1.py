class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False

studen1 = student("bharath1", 90)
print(studen1.name)
print(studen1.marks)
did_pass = studen1.check_pass_fail()
print(did_pass)
print("--------------------------------")
student2 = student("Hanuman", 30)
print(student2.name)
print(student2.marks)
did_pass = student2.check_pass_fail()
print(did_pass)
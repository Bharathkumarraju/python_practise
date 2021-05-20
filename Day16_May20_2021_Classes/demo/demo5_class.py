class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False

s1 = student("bk1", 35)
print(s1.name)
print(s1.marks)
did_pass = s1.check_pass_fail()
print(did_pass)

s2 = student("bk2", 90)
print(s2.name)
print(s2.marks)
did_pass = s2.check_pass_fail()
print(did_pass)
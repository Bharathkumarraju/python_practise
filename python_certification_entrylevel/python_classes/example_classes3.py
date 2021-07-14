class Grade:
    def __init__(self, subjects):
        self.subjects = subjects
    def print_sub(self):
        print(self.subjects)

grade1 = Grade(["maths", "science", "social"])
grade2 = Grade(["music", "biology", "viscom"])
grade3 = Grade(["test1", "test2", "test3"])

grade1.print_sub()
grade2.print_sub()
grade3.print_sub()



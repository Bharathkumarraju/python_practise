class grade:
    def __init__(self, subjects):
        self.subjects = subjects
    def print_sub(self):
        print(self.subjects)

grade1 = grade(['maths', 'science', 'history']) # Object initializes the class
grade2 = grade(['music', 'sports', 'psychology'])
grade3 = grade(['engineering', 'medicine'])

grade1.print_sub()
grade3.print_sub()
grade2.print_sub()



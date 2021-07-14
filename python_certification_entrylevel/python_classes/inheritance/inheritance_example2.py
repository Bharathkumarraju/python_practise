class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter


class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges")
        Polygon.display_info(self) # One way to call base class method
        super().display_info() # more elegant way do is using super() method.


class Quadrilateral(Polygon):
    def display_info(self):
        print("A Quadrilateral is a polygon with 4 edges")
        super().display_info()

t1 = Triangle([5, 6, 7])
perimeter=t1.get_perimeter()
print("perimeter is", perimeter)
t1.display_info()


q1 = Quadrilateral([1, 2, 3, 4])
perimeter=q1.get_perimeter()
print("perimeter is", perimeter)
q1.display_info()
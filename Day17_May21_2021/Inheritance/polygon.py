class polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter


class triange(polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges")
#        polygon.display_info(self)
        super().display_info()

class quadrilateral(polygon):
    def __init__(self):
        pass
    def display_info(self):
        print("A quadrilateral is a polygon with 4 edges")
        super().display_info()

t1 = triange([5, 6, 7])
perimeter = t1.get_perimeter()
print("Permitere is: ", perimeter)

t1.display_info()

q1 = quadrilateral()
q1.display_info()
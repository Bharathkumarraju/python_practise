from math import pi

def area_of_circle(r):
    if isinstance(r, str) or isinstance(r, complex):
        raise TypeError
    if r < 0:
        raise ValueError
    return pi * r * r

if __name__ == "__main__":
    radius = int(input("Enter radious of a circle: "))
    area =  area_of_circle(radius)
    print(f"Area of the circle is: ", area)
def area_of_square(**vars):
    b = vars["breadth"]
    h = vars["height"]
    return 1/2 * b * h

def main():
    b = int(input("Enter a breadth of a square"))
    h = int(input("enter a height of a square "))
    square_area =  area_of_square(breadth = b, height=h)
    print("Square of area is ", square_area)


if __name__ == '__main__':
    main()
def area_of_square(*vars):
    b = vars[0]
    h = vars[1]
    return 1/2 * b * h


def main():
    b = int(input("Enter a breadth of  square"))
    h = int(input("Enter height of a square"))
    square_area = area_of_square(b, h)
    print("Area of a square is: ", square_area)




if __name__ == '__main__':
    main()